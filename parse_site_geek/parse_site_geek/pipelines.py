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



        with open ("my_file.csv", 'a') as file:
            writer = csv.writer(file)
            writer.writerow(str_to_print)
        return item
