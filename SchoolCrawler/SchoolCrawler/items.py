# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SchoolcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  #标题
    url = scrapy.Field()  #对于互动百科页面的链接
    image = scrapy.Field()  #图片
    openTypeList = scrapy.Field()  #开放分类列表
    detail = scrapy.Field()  #详细信息
    baseInfoKeyList = scrapy.Field()  #基本信息key列表
    baseInfoValueList = scrapy.Field()  #基本信息value列表
