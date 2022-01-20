# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import csv

#збереження данних у файл csv
class ParseSiteGeekPipeline(object):
    def process_item(self, item, spider):

        print("Title: " + item["title"])
        print("News_text: " + "".join(item["news_text"]))
        print("Tegs: " + ", ".join(item["tegs"]))
        print("Link: " + item["link"])

        str_news = " ".join(item["news_text"])
        str_tegs = "#".join(item["tegs"])

        date_to_csv = item["date"].replace("/", "_")
        with open(f"{date_to_csv}.csv", 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='excel', delimiter=';')
            writer.writerow([item["title"], str_news, str_tegs, item["link"]])
        return item
