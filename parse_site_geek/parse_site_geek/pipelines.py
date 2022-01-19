# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import csv

class ParseSiteGeekPipeline(object):
    def process_item(self, item, spider):

        str_to_print = ";".join([item["title"], "".join(item["news_text"]), ", ".join(item["tegs"]), item["link"]])
        print("Title: " + item["title"])
        print("News_text: " + "".join(item["news_text"]))
        print("Tegs: " + ", ".join(item["tegs"]))
        print("Link: " + item["link"])

        date_to_csv = item["date"].replace("/", "_")
        with open(f"{date_to_csv}.csv", 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([str_to_print])
        return item
