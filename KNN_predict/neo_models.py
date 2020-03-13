# coding: utf-8

from py2neo import Graph,Node,Relationship,NodeMatcher
from read_csv import readCSV2
from hudong_class import HudongItem

class Neo4j():
	graph = None
	def __init__(self):
		print("create neo4j class ...")
		
	def connectDB(self):
		self.graph = Graph("http://localhost:7474/db/data/",username = 'neo4j',password = 'sherryice')
		
	def matchItembyTitle(self,value):
		matcher = NodeMatcher(self.graph)
		answer = matcher.match(label="Item").where('_.title =~'+'"'+value+'"').first()
		return answer

	# 根据title值返回互动百科item
	def matchHudongItembyTitle(self,value):
		matcher = NodeMatcher(self.graph)
		answer = matcher.match('HudongItem').where('_.title =~'+'"'+value+'"').first()
		return answer
		
	# 返回所有已经标注过的互动百科item   filename为labels.txt
	def getLabeledHudongItem(self, filename):
		labels = readCSV2(filename)
		List = []
		i = 0
		matcher = NodeMatcher(self.graph)
		for line in labels:
			ctx = matcher.match("HudongItem").where('_.title =~'+'"'+line[0]+'"').first()
			if ctx == None:
				continue;
			cur = HudongItem(ctx)
			cur.label = line[1]
			List.append(cur)
		
		print('load LabeledHudongItem over ...')
		return List
	
	# 返回限定个数的互动百科item
	def getAllHudongItem(self, limitnum):
		List = []
		ge = self.graph.find("HudongItem", limit=limitnum)
		for g in ge:
			List.append(HudongItem(g))
			
		print('load AllHudongItem over ...')
		return List

# test = Neo4j()
# test.connectDB()
# a = test.getLabeledHudongItem('labels1.txt')
# print(a[10].openTypeList)
# selector = NodeMatcher(test.graph)
# print(test.matchHudongItembyTitle("菊糖"))

