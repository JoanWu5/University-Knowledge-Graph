# coding: utf-8

from py2neo import Graph,Node,Relationship,NodeMatcher
from read_csv import readCSV2
from school_class import SchoolItem

class Neo4j():
	graph = None
	def __init__(self):
		print("create neo4j class ...")
		
	def connectDB(self):
		self.graph = Graph("http://localhost:7474/db/data/",username = 'neo4j',password = 'sherryice')

	# 根据title值返回互动百科item
	def matchSchoolItembyTitle(self,value):
		matcher = NodeMatcher(self.graph)
		answer = matcher.match('SchoolItem').where('_.title =~'+'"'+value+'"').first()
		return answer
		
	# 返回所有已经标注过的互动百科item   filename为labels1.txt
	def getLabeledSchoolItem(self, filename):
		labels = readCSV2(filename)
		List = []
		i = 0
		matcher = NodeMatcher(self.graph)
		for line in labels:
			ctx = matcher.match("SchoolItem").where('_.title =~'+'"'+line[0]+'"').first()
			if ctx == None:
				continue;
			cur = SchoolItem(ctx)
			cur.label = line[1]
			List.append(cur)
		
		print('load LabeledSchoolItem over ...')
		return List
	
	# 返回限定个数的互动百科item
	def getAllSchoolItem(self, limitnum):
		List = []
		ge = self.graph.find("SchoolItem", limit=limitnum)
		for g in ge:
			List.append(SchoolItem(g))
			
		print('load AllSchoolItem over ...')
		return List

# test = Neo4j()
# test.connectDB()
# # a = test.getLabeledSchoolItem('test.txt')
# # print(a[2].openTypeList)
# selector = NodeMatcher(test.graph)
# print(test.matchSchoolItembyTitle("《复旦学报（自然科学版）》"))

