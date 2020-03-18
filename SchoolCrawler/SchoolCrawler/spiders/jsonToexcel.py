#-*-coding:utf-8-*-
import csv
import json
import sys
import codecs
import os

os.chdir(r'E:\assignment\Thesis\University-Knowledge-Graph\SchoolCrawler\SchoolCrawler\spiders')

import csv
import json


def trans(jsonpath, csvpath):
    json_file = open(jsonpath, 'r', encoding='utf-8')
    csv_file = open(csvpath, 'w', newline='',encoding='utf-8')
    keys = []
    writer = csv.writer(csv_file)

    json_data = json_file.read()
    dic_data = json.loads(json_data, encoding='utf-8')

    for dic in dic_data:
        keys = dic.keys()
        # 写入列名
        writer.writerow(keys)
        break

    for dic in dic_data:
        for key in keys:
            if key not in dic:
                dic[key] = ''
        writer.writerow(dic.values())
    json_file.close()
    csv_file.close()

trans('school_pedia1.json','school_pedia1.csv')


