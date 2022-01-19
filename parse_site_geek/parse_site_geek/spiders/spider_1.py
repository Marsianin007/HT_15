import datetime
import scrapy

# from parse_site_geek.parse_site_geek.items import ParseSiteItem


def get_date():
    date_check = True
    valid_date = None
    date = input("Введіть дату у форматі yyyy/mm/dd: ")

    try:
        valid_date = datetime.datetime.strptime(date, '%Y/%m/%d')
    except ValueError:
        date_check = False

    if valid_date.date() > datetime.datetime.now().date():
        date_check = False

    return date_check, date


class ParseSiteItem(scrapy.Item):
    title = scrapy.Field()
    news_text = scrapy.Field()
    tegs = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()


class SiteSpider(scrapy.Spider):
    date, date_check = None, None

    def start_requests(self):
        SiteSpider.date_check, SiteSpider.date = get_date()
        while SiteSpider.date_check is False:
            SiteSpider.date_check, SiteSpider.date = get_date()
        else:
            yield scrapy.Request(url=self.start_urls[0] + str(SiteSpider.date), callback=self.parse)

    name = "site_spider"
    start_urls = ["https://www.vikka.ua/"]

    def parse(self, response):
        for link in response.xpath("//h2[@class='title-cat-post']//a/@href"):
            yield response.follow(link, callback=self.parse_news)

    def parse_news(self, response):
        item = ParseSiteItem()
        item["title"] = response.xpath("//h1[@class='post-title -margin-b']/text()").get()
        item["news_text"] = response.xpath("//div[@class='entry-content -margin-b']/p/text()").getall()
        item["tegs"] = response.xpath("//a[@class='post-tag']/text()").getall()
        item["link"] = response.url
        item["date"] = self.date
        yield item
