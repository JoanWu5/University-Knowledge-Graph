import json
from py2neo import Node, Relationship ,Graph
import re

class loadDatatoNeo4j(object):
    graph = None
    # def __init__(self):
    #     print("start load data ...")
    # def connectDB(self):
    #     self.graph = Graph("http://localhost:7474",username = "neo4j" , password = "sherryice")
    #     print("connect neo4j success!")

    def readData(self):
        with open("train_data.txt",'w',encoding='utf-8') as fw:
            fw.write('entity1\tentity2\trelation')
        with open("all_entity.txt",'r',encoding='utf-8') as fr_all:
            all_entity = []
            for line in fr_all:
                all_entity.append(line.strip())
        with open("exsit_entity.txt","r",encoding="utf-8") as fr_exsit:
            exsit_entity = []
            for line in fr_exsit:
                exsit_entity.append(line.strip())
        with open("new_entity.txt","r",encoding="utf-8") as fr_new:
            new_entity = []
            for line in fr_new:
                new_entity.append(line.strip())
        with open("new_entityRelation_zh.json","r",encoding='utf-8') as fr:
            with open("train_data.txt","w",encoding="utf-8") as fw:
                entityList = []
                for line in fr:
                    # print(line)
                    entityRelationJson = json.loads(line)
                    entity1 = entityRelationJson['entity1']
                    entity2 = entityRelationJson['entity2']
                    relation = entityRelationJson['relation']
                    if entity1 in all_entity and entity2 in all_entity and entity1!= entity2:
                        if not [entity1,entity2] in entityList:
                            fw.write(entity1+'\t'+entity2+'\t'+relation+'\n')
                        entityList.append([entity1,entity2])
                            

if __name__ == "__main__":
	loadData = loadDatatoNeo4j()
	loadData.readData()