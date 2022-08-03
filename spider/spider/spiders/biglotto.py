import scrapy

from spider.items import BigLottoItem

class BiglottoSpider(scrapy.Spider):
    name = 'biglotto'
    allowed_domains = ['datachart.500.com']
    start_urls = ['https://datachart.500.com/dlt/history/newinc/history.php?limit=100000&sort=0']

    def parse(self, response):
        data_list = response.xpath('//tr[@class="t_tr1"]/td/text()').extract()
        data_list = data_list[9:]
        while data_list:
            item = data_list[:15]
            data_list = data_list[15:]
            print(item)
            blt = BigLottoItem(number_one=item[1],
                               number_two=item[2],
                               number_three=item[3],
                               number_four=item[4],
                               number_five=item[5],
                               blue_one=item[6],
                               blue_two=item[7],
                               data_time=item[14])
            yield blt
