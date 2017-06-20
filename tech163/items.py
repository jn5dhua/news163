# -*- coding: utf-8 -*-
    # Define here the models for your scraped items
    #
    # See documentation in:
    # http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class Tech163Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_thread=Field() #新闻id
    news_title = Field()
    news_url = Field()
    news_time=Field()
    news_from=Field()   #新闻来源
    from_url=Field()    #来源网站
    news_content=Field()