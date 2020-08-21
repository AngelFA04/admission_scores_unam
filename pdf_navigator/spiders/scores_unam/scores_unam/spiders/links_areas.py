""" This spider extracts all the links of the UNAM careers from
 their Area page. After that it saves all those links in a JSON file"""
 import scrapy
 
 class SpiderLinkCareer(scrapy.Spider):
     name = 'area'


     def parse(self, response):
         pass

    def parse_links_careers(self, response):
        pass