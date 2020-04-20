# coding: utf-8
# 转化为词向量
from pyfasttext import FastText
import thulac
# from pre_load import pre_load_thu,neo_con,predict_labels
# from NER import get_NE,temporaryok

def create_predict():
	# thu1 = thulac.thulac()  #默认模式
	# statements = []
	# with open("all_entity.txt",'w',encoding='utf-8') as fw:
	# 	with open('train_data.txt','r',encoding='utf-8-sig') as fr:
	# 		entity = []
	# 		for line in fr:
	# 			statement = line.strip().split('\t')[2]
	# 			statements.append(statement)
	# 			cutResult = get_NE(statement)
	# 			for item in cutResult:
	# 				if item[0] in entity:
	# 					continue
	# 				else:
	# 					print(item[0],len(statements))
	# 					entity.append(item[0])
	# 					fw.write(item[0]+'\n')
	

	with open("all_entity_clean.txt",'r',encoding='utf-8') as fr:
		predict_List = []
		for line in fr:
			predict_List.append(line.strip())

	file_object = open('new_vector.txt','w',encoding='utf-8')

	model = FastText('wiki.zh.bin')
	
	count = 0

	for p in predict_List:
		count +=1
		wv_list = model[p]
		strr = str(p)
		for p in wv_list:
			strr += ' '+str(p)[:7]
		file_object.write(strr+"\n")
		print(str(count)+' / '+str(len(predict_List)))
		
	file_object.close()
	
create_predict()

# def clean_entity():
#     predict_List = []
#     with open("all_entity.txt","r",encoding="utf-8") as fr:
#         for line in fr:
#             line = line.strip().replace('「','').replace('」','').replace(' ','')
#             if line!='':
#                 predict_List.append(line)
#     print(len(predict_List))
#     predict_List = set(predict_List)
#     predict_List = [k for k in predict_List]
#     print(len(predict_List))
#     with open("all_entity_clean.txt","w",encoding="utf-8") as fw:
#         for i in predict_List:
#             fw.write(i+'\n')
# clean_entity()
        
    

	