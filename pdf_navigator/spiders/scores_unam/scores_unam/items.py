# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScoresUnamItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LinkArea():
    """
    Item to store the links from the areas and their data.
    """
    name = scrapy.Field()
    #Sometimes it is only found in the link
    link = scrapy.Field()
    area = scrapy.Field()

    pass

class Career():
    
    name = scrapy.Field()
    #Name and id
    faculty = scrapy.Field()
    area = scrapy.Field()
    modality = scrapy.Field()
    year = scrapy.Field()
    #Feb or Jun
    contest = scrapy.Field()
    #An array
    scores = scrapy.Field()
    #Extra data. Ofert, aspirants, actual_test, min score, selected 
    extra = scrapy.Field()
    link = scrapy.Field()
    pass
