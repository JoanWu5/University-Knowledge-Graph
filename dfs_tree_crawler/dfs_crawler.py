# -*- coding: utf-8 -*-  
import urllib.request  
from urllib.parse import quote
import re

pre_str = 'http://fenlei.baike.com/'

def getHtml(url):  
	url = quote(url, safe='/:?=')  # url处理中文
	page = urllib.request.urlopen(url)  
	html = page.read().decode(encoding='utf-8',errors='strict')  
	return html  
	
	
def dfs(u_str):
	print('entry: '+u_str)
	with open('treenode_list.txt','a',encoding= 'utf-8') as f:
		f.write(u_str+"\n")
	html = getHtml(pre_str + u_str)
	s = html.find('下一级微百科')
	if s == -1:
		return

	sublist = []   ## 得到了所有子概念名称的列表
	for i in range(s,999999999):
		if html[i]=='<' and html[i+1]=='/' and html[i+2]=='a':
			j = i
			while html[j]!= '>':
				j -= 1
			j += 1
			str = ''
			while j<i:
				str += html[j]
				j += 1
			sublist.append(str)
		
		if html[i]=='<' and html[i+1]=='/' and html[i+2]=='p' and html[i+3]=='>':
			break
	
	with open('micropedia_tree.txt','a',encoding= 'utf-8') as fm:
		if sublist!=[]:
			for item in sublist:
				fm.write(u_str+" "+item+"\n")

	for sub in sublist:
		dfs(sub)
	 
dfs('中国大学')
	
	