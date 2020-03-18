# coding: utf-8

from py2neo import Graph,Node,Relationship,NodeMatcher
from school_class import SchoolItem

class Neo4j():
	graph = None
	def __init__(self):
		print("create neo4j class ...")
		
	def connectDB(self):
		self.graph = Graph("http://localhost:7474", username="neo4j", password="sherryice")
		print('connect successed')
		
	def matchItembyTitle(self,value):
		matcher = NodeMatcher(self.graph)
		answer = matcher.match('Item').where('_.title =~'+'"'+value+'"').first()
		return answer

	# 根据title值返回互动百科item
	def matchSchoolItembyTitle(self,value):
		matcher = NodeMatcher(self.graph)
		answer = matcher.match('SchoolItem').where('_.title =~'+'"'+value+'"').first()
		return answer
			
	# 返回限定个数的互动百科item
	def getAllSchoolItem(self, limitnum):
		List = []
		ge = self.graph.find(label="SchoolItem", limit=limitnum)
		for g in ge:
			List.append(SchoolItem(g))
			
		print('load AllSchoolItem over ...')
		return List
		
		
