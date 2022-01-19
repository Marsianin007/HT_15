# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ParseSiteItem(scrapy.Item):
    title = scrapy.Field()
    news_text = scrapy.Field()
    tegs = scrapy.Field()
    link = scrapy.Field()
