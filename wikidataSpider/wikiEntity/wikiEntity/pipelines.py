# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

class WikientityPipeline(object):
    def __init__(self):
        self.file = open('all_entity_clean.json','w',encoding = 'utf-8')

    def process_item(self, item, spider):
        entityjson = json.dumps(dict(item),ensure_ascii=False) + '\n'
        print(entityjson)
        self.file.write(entityjson)
        return item


