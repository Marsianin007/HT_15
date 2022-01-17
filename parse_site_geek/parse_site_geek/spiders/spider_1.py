import scrapy
import datetime


def get_date():
    day, month, year = 0, 0, 0
    str_date = ""
    check_date = False
    date_datetime_format = None
    date = input("Ваша дата у форматі yyyy-mm-dd: ")
    print(date)
    dict_of_moths = {"1": "Січня", "2": "Лютого", "3": "Березеня", "4": "Квітеня", "5": "Травня", "6": "Червня",
                    "7": "Липня", "8": "Серпня", "9": "Вересня", "10": "Жовтня", "11": "Листопада", "12": "Грудня"}
    try:
        date_datetime_format = datetime.datetime.strptime(date, "%Y-%m-%d")
        day = date_datetime_format.day
        month = date_datetime_format.month
        month = dict_of_moths[str(month)]
        year = date_datetime_format.year
        str_date = str(day) + " " + month + " " + str(year)
        check_date = True
    except:
        print("Невірна дата")
        get_date()

    if date_datetime_format.strftime("%Y%m%d") > datetime.datetime.now().strftime("%Y%m%d"):
        check_date = False
        print("Невірна дата")
        get_date()

    return check_date, str_date, day, month, year


check_date, str_date, day, month, year = get_date()

if check_date:
    class NewsParser(scrapy.Spider):
        name = "site_spider"
        start_urls = ["https://www.vikka.ua/category/novini/"]

        def parse(self, response):
            for link in response.xpath("//ul[@class='cat-posts-wrap margin-b-40 blogs-category']//a/@href"):
                yield response.follow(link, callback=self.parse_site)

        def parse_site(self, response):
            date = response.xpath("//span[@class='post-info-style']/text()").get()
            date = date.split()
            dict_tmp =  {
                "title" : response.xpath("//h1[@class='post-title -margin-b']/text()").get(),
                "news_text" : response.xpath("//div[@class='entry-content -margin-b']//p/text()").get(),
                "tegs" : response.xpath("//a[@class='post-tag']//text()").get()

            }
            date_from_web = str(date[0]) + " " + str(date[1]) + " " + str(date[2])
            if str_date == date_from_web:
                string_to_put = dict_tmp["title"] + "," + dict_tmp["news_text"] + "," + dict_tmp["tegs"] + "\n"
                with open(f"{str_date}.csv", "a+") as file:
                    file.write(string_to_put)










