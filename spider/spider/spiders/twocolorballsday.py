import scrapy


from spider.items import TwoColorBallItem


class TwocolorballsDaySpider(scrapy.Spider):
    name = 'twocolorballsday'
    allowed_domains = ['datachart.500.com']
    start_urls = ['https://datachart.500.com/ssq/history/newinc/history.php?limit=5&sort=0']

    def parse(self, response):
        data_list = response.xpath('//tr[@class="t_tr1"]/td/text()').extract()
        while data_list:
            item = data_list[:16]
            data_list = data_list[16:]
            print(item)
            tcb = TwoColorBallItem(number_one=item[1],
                                   number_two=item[2],
                                   number_three=item[3],
                                   number_four=item[4],
                                   number_five=item[5],
                                   number_six=item[6],
                                   number_blue=item[7],
                                   data_time=item[15])
            yield tcb
