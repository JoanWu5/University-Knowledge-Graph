# coding: utf-8
from classifier import Classifier
from neo_models import Neo4j
from read_csv import readCSVbyColumn
from school_class import SchoolItem

def create_predict(SchoolItem_csv):
	# 读取neo4j内容 
	db = Neo4j()
	db.connectDB()
	data_set = db.getLabeledSchoolItem('labels1.txt')
	classifier = Classifier('wiki.zh.bin')
	classifier.load_trainSet(data_set)     
	classifier.set_parameter(weight=[1.0, 3.0, 0.2, 4.0, 0],k=9)
	predict_List = readCSVbyColumn(SchoolItem_csv, 'title')
	file_object = open('predict_labels.txt','a',encoding='utf-8')
	
	count = 0
	vis = set()
	for p in predict_List:
		cur = SchoolItem(db.matchSchoolItembyTitle(p))
		count += 1
		title = cur.title
		if title in vis:
			continue
		vis.add(title)
		label = classifier.KNN_predict(cur)
		print(str(title)+" "+str(label)+": "+str(count)+"/"+str(len(predict_List)))
		file_object.write(str(title)+" "+str(label)+"\n")
		
	file_object.close()
	
create_predict('school_pedia.csv')
	