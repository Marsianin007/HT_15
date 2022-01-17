# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader



class ParseSiteGeekItem(scrapy.Item):
    title = scrapy.Field()
    news_text = scrapy.Field()
    tegs = scrapy.Field()


class SiteItemLoader(ItemLoader):
    pass
