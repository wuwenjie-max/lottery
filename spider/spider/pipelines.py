# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class SpiderPipeline:
    def open_spider(self, spider):
        if spider.name == 'twocolorballs':
            file_name = 'twocolorballs.csv'
            field_names = ['number_one', 'number_two', 'number_three', 'number_four', 'number_five', 'number_six', 'number_blue', 'data_time']
        elif spider.name == 'biglotto':
            file_name = 'biglotto.csv'
            field_names = ['number_one', 'number_two', 'number_three', 'number_four', 'number_five', 'blue_one', 'blue_two', 'data_time']
        else:
            raise ValueError('unkown')
        if os.path.exists(file_name):
            os.remove(file_name)
        _fp = open(file_name, 'x', encoding='utf-8')
        self.fp = csv.DictWriter(_fp, fieldnames=field_names)
        self.fp.writeheader()

    def process_item(self, item, spider):
        self.fp.writerow(item)
        return item

    def close_spider(self, spider):
        print('spider success')
