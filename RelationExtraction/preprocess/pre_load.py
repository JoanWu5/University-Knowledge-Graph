# -*- coding: utf-8 -*-
import thulac
import csv
import sys
import os


from neo_models import Neo4j 
from mongo_model import Mongo

	
pre_load_thu = thulac.thulac()  #默认模式
print('thulac open!')

neo_con = Neo4j()   #预加载neo4j
neo_con.connectDB()
print('neo4j connected!')

predict_labels = {}   # 预加载实体到标注的映射字典
filePath = os.getcwd()
with open('predict_labels_accurate.txt','r',encoding="utf-8") as csvfile:
	reader = csv.reader(csvfile, delimiter=' ')
	for row in reader:
		predict_labels[str(row[0])] = int(row[1])
print('predicted labels load over!')

		
# 预加载mongodb
mongo = Mongo()
mongo.makeConnection()
print("mongodb connected")
#连接数据库
mongodb = mongo.getDatabase("SchoolKnowledgeGraph")
print("connect to SchoolKnowledgeGraph")
# 得到collection
collection = mongo.getCollection("train_data")
print("get connection train_data")

testDataCollection = mongo.getCollection("test_data")
print("get connection test_data")