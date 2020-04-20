# -*- coding: utf-8 -*-

import os
import thulac
import sys
import json
from pre_load import pre_load_thu,neo_con,predict_labels
from NER import get_NE,temporaryok

# 分句标识符号
stopToken = "。！？"
def CutStatements(line):
	statements = []
	tokens = []
	for token in line:
		tokens.append(token)
		#如果是句子停止词
		if(token in stopToken):			
			statements.append(''.join(tokens))
			tokens = []
	if(len(tokens)>2 ):
		statements.append(''.join(tokens)+"。")
	return statements

thu = thulac.thulac() #预先加载好
corpusPath = os.path.abspath(os.path.join(os.getcwd(),"data/"))
#获取已经处理过得文件
fileReadedList = []
with open("fileReaded.txt","r",encoding='utf-8') as fileReaded:
	for line in fileReaded:
		fileReadedList.append(line.strip())
		print(line.strip())
#递归遍历语料库文件夹
with open("result/train_data.txt",'w',encoding='utf-8') as fw:
	with open("fileReaded.txt","a",encoding='utf-8') as filereaded:	
		for root,dirs,files in os.walk(corpusPath):			
			for file in files:
				print(file)
				filePath = os.path.join(root,file)
				if(filePath in fileReadedList):
					continue
				if len(file) >0:
					with open(filePath,'r',encoding='utf-8') as fr:
						count = 0
						for line in fr:
							#分句
							statements = CutStatements(line)
							for statement in statements:
								#分词
								cutResult = get_NE(statement.strip())
								print(cutResult)
								if cutResult!=[]:
									cutResult = set(k[0] for k in cutResult)
									print(cutResult)
									for result1 in cutResult:
										fw.write(result1+'\t')
								fw.write('\n')
									
					filereaded.write(filePath+'\n')

