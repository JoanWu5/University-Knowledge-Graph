# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
import thulac
 
import sys
sys.path.append("..")
from toolkit.pre_load import neo_con
from toolkit.pre_load import wv_model, tree ,predict_labels
from toolkit.NER import get_explain,get_detail_explain

# 接收GET请求数据
def showdetail(request):
	ctx = {}
	if 'title' in request.GET:
		# 连接数据库
		db = neo_con
		
		title = request.GET['title']
		answer = db.matchSchoolItembyTitle(title)
		if answer == None:
			return render(request, "404.html", ctx) 

		if len(answer) > 0:
			answer = answer[0]['n']
		else:
			ctx['title'] = '实体条目出现未知错误'
			return

		ctx['detail'] = answer['detail']
		ctx['title'] = answer['title']
		image = answer['image']
		
		ctx['image'] = '<img src="' + str(image) + '" alt="该条目无图片" height="100%" width="100%" >'
		
		ctx['baseInfoKeyList'] = []
		if answer['baseInfoKeyList']:
			List = answer['baseInfoKeyList'].split('##')
			for p in List:
				ctx['baseInfoKeyList'].append(p)
			
		ctx['baseInfoValueList'] = []
		if answer['baseInfoValueList']:
			List = answer['baseInfoValueList'].split('##')
			for p in List:
				ctx['baseInfoValueList'].append(p)
			
		text = ""
		if answer['openTypeList']:
			List = answer['openTypeList'].split('##')
			for p in List:
				text += '<span class="badge bg-important">' + str(p) + '</span> '
		ctx['openTypeList'] = text
		
		text = '<table class="table table-striped table-advance table-hover"> <tbody>'
		if answer['baseInfoKeyList']:
			keyList = answer['baseInfoKeyList'].split('##')
			valueList = answer['baseInfoValueList'].split('##')
			i = 0
			while i < len(keyList) :
				value = " "
				if i < len(valueList):
					value = valueList[i]
				text += "<tr>"
				text += '<td><strong>' + keyList[i] + '</strong></td>'
				text += '<td>' + value + '</td>'
				i += 1
				
				if i < len(valueList):
					value = valueList[i]
				if i < len(keyList) :
					text += '<td><strong>' + keyList[i] + '</strong></td>'
					text += '<td>' + value + '</td>'
				else :
					text += '<td><strong>' + '</strong></td>'
					text += '<td>' + '</td>'
				i += 1
				text += "</tr>"
			text += " </tbody> </table>"
			if answer['baseInfoKeyList'].strip() == '':
				text = ''
		ctx['baseInfoTable'] = text 
		
		tagcloud = ""
		taglist = wv_model.get_simi_top(answer['title'], 10)
		for tag in taglist:
			tagcloud += '<a href= "./detail.html?title=' + str(tag) + '"> '
			tagcloud += str(tag) + "</a>"
#			print(tag)
		ctx['tagcloud'] = tagcloud
		
		school_type = ""
		ansList = tree.get_path(answer['title'], True)
		for List in ansList:
			school_type += '<p >'
			flag = 1
			for p in List:
				if flag == 1:
					flag = 0
				else:
					school_type += ' / '
				school_type += str(p)
				
			school_type += '</p>'	
		if len(ansList) == 0:
			school_type = '<p > 暂无高校类型</p>'
		ctx['school_type'] = school_type	
		
		entity_type = ""
		explain = get_explain(predict_labels[answer['title']])
		detail_explain = get_detail_explain(predict_labels[answer['title']])
		entity_type += '<p > [' + explain + "]: "
		entity_type += detail_explain + "</p>"
		ctx['entity_type'] = entity_type	
			
	else:
		return render(request, "404.html", ctx) 		
			
	return render(request, "detail.html", ctx)
	