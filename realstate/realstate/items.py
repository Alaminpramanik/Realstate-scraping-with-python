# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealtorItem(scrapy.Item):
    # define the fields for your item here like:

    Photo = scrapy.Field()
    Title = scrapy.Field()
    City = scrapy.Field()
    Surface = scrapy.Field()
    Number_of_room = scrapy.Field()
    Kalmiete = scrapy.Field()
    Nebenkosten = scrapy.Field()
    Garage = scrapy.Field()
    Genossenschafts = scrapy.Field()
    Heizkosten = scrapy.Field()
    Netrent = scrapy.Field()
    Compition = scrapy.Field()
    Online = scrapy.Field()



