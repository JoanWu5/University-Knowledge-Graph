# -*- coding: utf-8 -*-
import json

## 先生成一部分很明显的标签

def read_word():
	file_object = open('crawled_leaf_list1.txt','r',encoding='utf-8')
	all_list = []
	for f in file_object:
		all_list.append(f)
	return all_list
	
# 标注不合法数据
def is_num(s):
	flag = True
	for p in s:
		if p>='0' and p<='9':
			pass
		else:
			flag = False
	return flag

def only_num_letter(s):
	flag = True
	for p in s:
		if p>='0' and p<='9':
			pass
		elif p=='零' or p=='一' or p=='二' or p=='三' or p=='四' or p=='五' or p=='六' or p=='七' or p=='八'or p=='九' or p=='十':
			pass
		elif p=='百'or p=='千'or p=='万'or p=='亿':
			pass
		else:
			flag =False
	return flag	
		
def create_invalid():
	all_list = read_word()
	file_object = open('invalid2.txt','w')
#	for word in all_list:
#		word = word.strip() #需要把\n去除
#		if word[len(word)-1] == '年':
#			file_object.write(word+" 0\n")
	for word in all_list:
		word = word.strip()
		if only_num_letter(word):
			file_object.write(word+" 0\n")
	file_object.close()
	
#create_invalid()
	
# 标注人物
def surname_table():
	table = set({'李','王','张','刘','陈','杨','赵','周','吴','徐','孙','胡','朱','何','郭','潘','苏','马'})
	#李、王、张、刘、陈、杨、赵、黄、周、吴、徐、孙、胡、朱、高、林、何、郭和马
	return table
	
def create_person():  ##最后还是只检查了100个，因为姓名很容易看错
	all_list = read_word()
	file_object = open('person1.txt','w',encoding='utf-8')
	surname = surname_table()
	for word in all_list:
		word = word.strip()
		if word[0] in surname and len(word)<=4 :
			file_object.write(word+" 1\n")
	file_object.close()

# create_person()

# 标注地点
def loc_table():
	table = set({'国','市','区','县','省','街','路'})
	return table
	
def create_location():  ##只检查了200个
	all_list = read_word()
	file_object = open('location1.txt','w',encoding='utf-8')
	loc = loc_table()
	for word in all_list:
		word = word.strip()
		if word[len(word)-1] in loc :
			file_object.write(word+" 2\n")
	file_object.close()

create_location()

# 标注机构
def is_org(s):
	table = set({'大学','学院','委员会','公司','大会','协会','研究院','中心','社'})
	if '大学' in s or '学院' in s or '委员会' in s or '公司' in s or '大会' in s or '协会' in s or '研究院' in s or '中心' in s or '社' in s:
		return True
	return False
	
def create_organization():  ##
	all_list = read_word()
	file_object = open('organization1.txt','w',encoding='utf-8')
	for word in all_list:
		word = word.strip()
		if is_org(word) :
			file_object.write(word+" 3\n")
	file_object.close()
	
# create_organization()

def is_web(s):
	table = set({'网','吧','BBS','论坛'})
	if '网' in s or '吧' in s or 'BBS' in s or '论坛' in s:
		return True
	return False

#标注网站
def create_website():
	all_list = read_word()
	file_object = open('website.txt','w',encoding='utf-8')
	for word in all_list:
		word = word.strip()
		if is_web(word):
			file_object.write(word+" 4\n")
	file_object.close()

# create_website()

#标注奖项
def is_award(s):
	table = set({'奖'})
	if '奖'in s:
		return True
	return False

def create_award():
	all_list = read_word()
	file_object = open('award.txt','w',encoding='utf-8')
	for word in all_list:
		word = word.strip()
		if is_award(word):
			file_object.write(word+" 5\n")
	file_object.close()

# create_award()

#标注专业
def is_major(s):
	table = set({'系','专业'})
	if '系' in s or '专业' in s:
		return True
	return False

def create_major():
	all_list = read_word()
	file_object = open('major.txt','w',encoding='utf-8')
	for word in all_list:
		word = word.strip()
		if is_major(word):
			file_object.write(word+" 6\n")
	file_object.close()

# create_major()

#注明告示
def is_notice(s):
	table= set({'通知','规定','公告','安排','公示'})
	if '通知' in s or '规定' in s or '公告' in s or '公示' in s or '安排' in s:
		return True
	return False

def create_notice():
	all_list = read_word()
	file_object = open('notice.txt','w',encoding='utf-8')
	for word in all_list:
		word = word.strip()
		if is_notice(word):
			file_object.write(word+" 7\n")
	file_object.close()

# create_notice()

#注明活动
def is_activity(s):
	table = set({'活动','赛','杯'})
	if '活动' in s or '赛' in s or '杯' in s:
		return True
	return False

def create_activity():
	all_list = read_word()
	file_object = open('activity.txt','w',encoding='utf-8')
	for word in all_list:
		word = word.strip()
		if is_activity(word):
			file_object.write(word+" 8\n")
	file_object.close()

# create_activity()

