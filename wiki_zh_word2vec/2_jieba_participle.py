#!/usr/bin/env python
# -*- coding: utf-8  -*-
#逐行读取文件数据进行jieba分词

import jieba
import jieba.analyse
import jieba.posseg as pseg #引入词性标注接口 
import codecs,sys
import re

def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False
    
if __name__ == '__main__':
    f = codecs.open('wiki.zh.simp.txt', 'r', encoding='utf8')
    target = codecs.open('all_chinese_entity.txt', 'a', encoding='utf8')
    print('open files.')

    lineNum = 1
    line = f.readline()
    while line:
        print ('---processing ',lineNum,' article---')
        seg_list = jieba.cut(line.strip(),cut_all=False)
        TagList = list(seg_list)
        i = 0
        while i<len(TagList):
            p1 = TagList[i]
            p1 = p1.replace('(','（').replace(')','）').replace('*','').replace('-','').replace('+','').replace('^','').replace('/','').replace('%','').replace('=','').replace('~','').replace('<','').replace('>','').replace('{','').replace('}','').replace('[','').replace(']','').replace('?','').replace('「','').replace('」','').replace(' ','')
            p1 = re.sub('\"','',p1).strip()
            if p1!=''and is_Chinese(p1):
                target.writelines(p1+'\n')
            i+=1
        lineNum = lineNum + 1
        line = f.readline()

    print ('well done.')
    f.close()
    target.close()
