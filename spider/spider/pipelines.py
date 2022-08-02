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
        if os.path.exists('data.csv'):
            os.remove('data.csv')
        _fp = open('data.csv', 'x', encoding='utf-8')
        self.fp = csv.DictWriter(_fp, fieldnames=['number_one', 'number_two', 'number_three', 'number_four', 'number_five', 'number_six', 'number_blue', 'data_time'])
        self.fp.writeheader()

    def process_item(self, item, spider):
        self.fp.writerow(item)
        return item

    def close_spider(self, spider):
        print('spider success')
