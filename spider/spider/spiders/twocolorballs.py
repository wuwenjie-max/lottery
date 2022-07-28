import scrapy


class TwocolorballsSpider(scrapy.Spider):
    name = 'twocolorballs'
    allowed_domains = ['datachart.500.com']
    start_urls = ['http://datachart.500.com/']

    def parse(self, response):
        divList = response.xpath('//div[@class="work-list-box"]/div')
        print(len(divList))
