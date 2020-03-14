# coding: utf-8
# 将csv转化为词向量
from neo_models import Neo4j
from read_csv import readCSVbyColumn
from school_class import SchoolItem
from pyfasttext import FastText

def create_predict(SchoolItem_csv):
	# 读取neo4j内容 
	db = Neo4j()
	db.connectDB()
	
	predict_List = readCSVbyColumn(SchoolItem_csv, 'title')
	file_object = open('vector.txt','a',encoding='utf-8')
	
	model = FastText('wiki.zh.bin')
	
	count = 0
	vis = set()
	for p in predict_List:
		cur = SchoolItem(db.matchSchoolItembyTitle(p))
		count += 1
		title = cur.title
		if title in vis:
			continue
		vis.add(title)
		wv_list = model[title]
		strr = str(title)
		for p in wv_list:
			strr += ' '+str(p)[:7]
		file_object.write(strr+"\n")
		print(str(count)+' / '+str(len(predict_List)))
		
	file_object.close()
	
create_predict('school_pedia.csv')
	