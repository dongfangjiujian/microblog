# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PicItem(scrapy.Item):
    image_url = scrapy.Field()
    category_title = scrapy.Field()
    category_url=scrapy.Field()

class NewspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
