# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
import thulac
 
import sys
sys.path.append("..")
from toolkit.pre_load import neo_con

# 数据标注页面的view
# 接收GET请求数据
def showtagging_data(request):
	ctx = {}
	if 'title' in request.GET:
		# 连接数据库
		db = neo_con
		title = request.GET['title']
		answer = db.matchSchoolItembyTitle(title)
		if answer == None:
			ctx['title'] = '<h1> 该url不存在，别乱搞！ </h1>'
			return render(request, "tagging_data.html", ctx)
		ctx['detail'] = answer['detail']
		ctx['title'] = answer['title']
		image = answer['image']
		
		ctx['image'] = '<img class="rounded card-img-top img-fluid" src="' + str(image) + '" alt="该条目无图片" style="width:30%" >'
		
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
				text += '<span class="badge badge-success">' + str(p) + '</span> '
		ctx['openTypeList'] = text
		
		text = ""
		if answer['baseInfoKeyList']:
			keyList = answer['baseInfoKeyList'].split('##')
			valueList = answer['baseInfoValueList'].split('##')
			i = 0
			while i < len(keyList) :
				value = " "
				if i < len(valueList):
					value = valueList[i]
				text += "<tr>"
				text += '<td class="font-weight-bold">' + keyList[i] + '</td>'
				text += '<td>' + value + '</td>'
				i += 1
				
				if i < len(valueList):
					value = valueList[i]
				if i < len(keyList) :
					text += '<td class="font-weight-bold">' + keyList[i] + '</td>'
					text += '<td>' + value + '</td>'
				else :
					text += '<td class="font-weight-bold">' + '</td>'
					text += '<td>' + '</td>'
				i += 1
				text += "</tr>"
		ctx['baseInfoTable'] = text
		
		## 动态生成check控件----------------------------------
		
		text = ""
		tag_name_list = []
		tag_name_list.append('Invalid（不合法，不是具体的实体，或一些脏数据）')
		tag_name_list.append('Person（人物，职位）')
		tag_name_list.append('Location（地点，区域）')
		tag_name_list.append('Organization（机构，会议）')
		tag_name_list.append('Website（大学相关网站，贴吧，BBS）')
		tag_name_list.append('Award（奖）')
		tag_name_list.append('Major（系，专业）')
		tag_name_list.append('Notice（通知，公告）')
		tag_name_list.append('Activity（活动，比赛）')
		tag_name_list.append('other（除上面类别之外的其它名词实体，可以与大学无关但必须是实体）')
		
		count = 0
		for i in range(len(tag_name_list)):
			text += '<div class="radio"> <label class="form-check-label">'
			text += '<input type="radio" name="label" value="' + str(i) + '">'
			text +=  str(count) + '. ' + tag_name_list[i]
			text += '</label>  </div>'
			count += 1
			
		# 放置一个隐藏的输入框，传递title的值到缓冲页面
		text += '<input name="title" value="' + str(answer['title']) + '"  style="display:none;" ></input>'
		ctx['taggingCheck'] = text
		
		
		# 统计当前标注情况
		file_object = open('label_data/labels1.txt','r',encoding='utf-8')
		s = []
		sum = 0
		for i in range(10):
			s.append(set())
		for f in file_object:
			pair = f.split()
			s[int(pair[1].strip())].add(pair[0].strip())
		for i in range(10):	
			sum += len(s[i])
		file_object.close()
		text = "" ##用于记录已标注样本个数
		for i in range(10):
			text += '<p>' + str(i) + '类: ' + str(len(s[i])) + '个</p>'
		text += '<p>总计: ' + str(sum) + '个</p>'
		ctx['already'] = text

				
	return render(request, "tagging_data.html", ctx)
	