# -*- coding: utf-8 -*-
import scrapy
from ..items import RealtorItem
import logging


class RealtorSpiderSpider(scrapy.Spider):
    name = 'real'
    # allowed_domains = ['realtor.com']
    start_urls = ['https://www.immobilienscout24.de/expose/67476373?referrer=RESULT_LIST_LISTING&navigationServiceUrl=%2FSuche%2Fcontroller%2FexposeNavigation%2Fnavigate.go%3FsearchUrl%3D%2FSuche%2Fshape%2Fwohnung-mieten%3Fshape%253DZ2ZtaUhlbnxzQHRFZUJLUWh1QHdCdlhzXnhHe1lySXdKaUphaUFtR2NXYkJlWHVLa0tJcU5sR3tLfUN0QW1Gd1F5eEB5bEFxVW5GZkR6WXdGblVnSmZKZUJ0UFVwYURoS25jQG5BYl4.%2526livingspace%253D50.0-70.0%2526enteredFrom%253Dsaved_search%26exposeId%3D67476373&navigationHasPrev=true&navigationBarType=RESULT_LIST&searchId=401ee836-83ad-31d2-bc03-13f5296a848c&searchType=drawn_area#/']

    def parse(self, response):
        items = RealtorItem()

        Photo = response.css('.gallery-element::attr(src)').extract()
        Title = response.css('#expose-title::text').extract()
        City = response.css('.one-half .zip-region-and-country::text').extract()
        Surface = response.css('.is24qa-flaeche::text').extract()
        Number_of_room = response.css('.is24qa-zi::text').extract()
        Kalmiete = response.css('.is24qa-kaltmiete.three-fifths::text').extract()
        Nebenkosten = response.css('.is24qa-nebenkosten::text').extract()
        Garage = response.css('.is24qa-miete-fuer-garagestellplatz::text').extract()
        Genossenschafts = response.css('.is24qa-kaution-o-genossenschaftsanteile::text').extract()
        Heizkosten = response.css('.is24qa-heizkosten::text').extract()
        Netrent = response.css('.is24qa-kaltmiete.font-semibold::text').extract()
        Compition = response.css('#chances-temperature-bar-container .align-center::text').extract()
        Online = response.css('div .style__statsBoxAmount___2VMws::text').extract()

        items['Photo'] = Photo
        items['Title'] = Title
        items['City'] = City
        items['Surface'] = Surface
        items['Number_of_room'] = Number_of_room
        items['Kalmiete'] = Kalmiete
        items['Nebenkosten'] = Nebenkosten
        items['Garage'] = Garage
        items['Genossenschafts'] = Genossenschafts
        items['Heizkosten'] = Heizkosten
        items['Netrent'] = Netrent
        items['Compition'] = Compition
        items['Online'] = Online



        yield items
