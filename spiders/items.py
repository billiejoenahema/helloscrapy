# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyproductsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    thumbnail = scrapy.Field()
    keyword = scrapy.Field()
    detail_link = scrapy.Field()
    page_count = scrapy.Field()
    url = scrapy.Field()
    timestamp = scrapy.Field()

    # pass