import json
from py2neo import Node, Relationship ,Graph,NodeMatcher
import re
class loadDatatoNeo4j(object):
	graph = None
	def __init__(self):
		print("start load data ...")
	def connectDB(self):
		self.graph = Graph("http://localhost:7474",username = "neo4j" , password = "sherryice")
		print("connect neo4j success!")

	def readData(self):
		count = 0
		with open("new_node.csv",'w',encoding='utf-8') as fw:
			fw.write("title,lable"+'\n')
		with open("new_wikidata_relation.csv","w",encoding='utf-8') as fw:
			fw.write("SchoolItem1,relation,SchoolItem2"+'\n')
		with open("new_wikidata_relation2.csv","w",encoding='utf-8') as fw:
			fw.write("SchoolItem,relation,NewNode"+'\n')
		with open("new_entityRelation_zh.json","r",encoding='utf-8') as fr:
			with open("new_node.csv",'a',encoding='utf-8') as fwNewNode:
				with open("new_wikidata_relation.csv",'a',encoding='utf-8') as fwWikidataRelation:
					with open("new_wikidata_relation2.csv",'a',encoding='utf-8') as fwWikidataRelation2:
						newNodeList = list()
						for line in fr:
							# print(line)
							entityRelationJson = json.loads(line)
							entity1 = entityRelationJson['entity1']
							entity2 = entityRelationJson['entity2']
							#搜索entity1
							matcher = NodeMatcher(self.graph)
							find_entity1_result = matcher.match('SchoolItem').where('_.title =~'+'"'+entity1+'"').first()
							#搜索entity2
							find_entity2_result = matcher.match('SchoolItem').where('_.title =~'+'"'+entity2+'"').first()
							count += 1
							print(count)
							# 如果entity1不在实体列表中(emmmmmm,不可能吧)，那么就不要继续了
							if(find_entity1_result is None):
								continue

							#去掉entityRelationJson['relation']中的逗号和双引号
							entityRelationList = re.split(",|\"",entityRelationJson['relation'])
							entityRelation = ""
							for item in entityRelationList:
								entityRelation = entityRelation + item
							#去掉entity2字符串中的逗号,并将繁体转成简体
							entity2List = re.split(",|\"",entity2)
							entity2 = "" 
							for item in entity2List:
								entity2 = entity2 + item

							# 如果entity2既不在实体列表中，又不在NewNode中，则新建一个节点，该节点的lable为newNode，然后添加关系
							if(find_entity2_result is None):
								if(entity2 not in newNodeList):
									fwNewNode.write(entity2+","+"newNode"+'\n')
									newNodeList.append(entity2)
								fwWikidataRelation2.write(entity1+","+entityRelation+","+entity2+'\n')
							#如果entity2在实体列表中，直接连关系即可
							else:
								fwWikidataRelation.write(entity1+","+entityRelation+","+entity2+'\n')



if __name__ == "__main__":
	loadData = loadDatatoNeo4j()
	loadData.connectDB()
	loadData.readData()









		
