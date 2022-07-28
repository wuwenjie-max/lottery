# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TwoColorBallItem(scrapy.Item):
    number_one = scrapy.Field()
    number_two = scrapy.Field()
    number_three = scrapy.Field()
    number_four = scrapy.Field()
    number_five = scrapy.Field()
    number_six = scrapy.Field()
    number_blue = scrapy.Field()
    data_time = scrapy.Field()

class BigLottoItem(scrapy.Item):
    number_one = scrapy.Field()
    number_two = scrapy.Field()
    number_three = scrapy.Field()
    number_four = scrapy.Field()
    number_five = scrapy.Field()
    blue_one = scrapy.Field()
    blue_two = scrapy.Field()
    data_time = scrapy.Field()


