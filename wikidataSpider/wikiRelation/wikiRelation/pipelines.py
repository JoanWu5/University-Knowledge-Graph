# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import copy

class WikirelationPipeline(object):
	def __init__(self):
		self.file = open('entityRelation.json','w',encoding = 'utf-8')
		self.file2 = open('entity1_entity2.json','w', encoding = 'utf-8')

	def process_item(self, item, spider):
		print(item)
		entityRelationItem = copy.deepcopy(item)
		entityRelationItem.pop("relatedEntityId")
		entityJson = json.dumps(dict(entityRelationItem),ensure_ascii=False) + '\n'
		entityIdItem = copy.deepcopy(item)
		entityIdItem.pop("entity2")
		entityIdItem.pop("relation")
		entityIdJson = json.dumps(dict(entityIdItem),ensure_ascii = False) + '\n' 
		self.file.write(entityJson)
		self.file2.write(entityIdJson)
		return item
