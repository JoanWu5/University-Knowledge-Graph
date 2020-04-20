# -*- coding: utf-8 -*-
# 得到需要的一些json数据
import os
import json
import numpy as np
import random

class get_json_file():
    def __init__(self):
        self.relation_file_name = 'new_staticResult.txt'
        self.relation_json_file_name = 'rel2id.json'
        self.dataset_file_name = 'train_data.txt'
        self.dataset_json_file_name = 'dataset.json'
        self.word2vec_file_name = 'new_vector_50.txt'
        self.word2vec_np_file_name = 'word2vec.npy'
        self.entity_json_file_name = 'all_entity_clean.txt'
        self.word2id_json_file_name = 'word2id.json'

    def get_rel_json(self):
        rel2id  = {'NA':0}
        relation_list = ['instance of','subclass of', 'part of','has effect','educated at']

        #rel2id = {}
        count = 1
        for x in relation_list:
            rel2id[x] = count
            count +=1

        with open(self.relation_json_file_name,'w') as fw:
            json.dump(rel2id,fw,ensure_ascii=False,indent = 4, separators=(',', ': '))

    def get_dataset_json(self):
        dataset = []
        entityList = {}
        count = 0
        with open(self.entity_json_file_name,'r',encoding='utf-8') as fr:
            for line in fr:
                entityList[line.strip()]= "Q"+str(count)
                count +=1 

        
        with open(self.dataset_file_name,'r',encoding='utf-8-sig') as fr:
            for line in fr.readlines():
                # print(line.strip().split('\t'))
                head,tail,sentence,relation = line.strip().split('\t')
                headpos_start = sentence.find(head)
                headpos_end = headpos_start+len(head)
                tailpos_start = sentence.find(head)
                tailpos_end  = tailpos_start+len(tail)
                print(head,tail)
                dataset.append({'h':{'pos':[headpos_start,headpos_end] , 'name':head.strip(),'id':entityList[head]} , 'relation':relation.strip(), 'text':sentence.strip(),'t':\
                    {'pos':[tailpos_start,tailpos_end],'name':tail.strip(),'id':entityList[tail]} } )
        with open(self.dataset_json_file_name,'w',encoding='utf-8') as fw:
            json.dump(dataset,fw,ensure_ascii=False,separators=(',', ': '))

    def get_word2vec_json(self):
        word2vec = []
        with open(self.word2vec_file_name,'r',encoding = 'utf-8') as fr:
            for line in fr:
                index = line.find(' ')
                word = line[0:index]
                vec = line[index:-1].strip().split()
                for index in range(len(vec)):
                    vec[index] = float(vec[index])
                word2vec.append(vec)

        np.save(self.word2vec_np_file_name,word2vec)

    def train_test_split(self):
        with open('dataset.json', 'r', encoding='utf-8') as fr:
            dataset = json.load(fr)

        dataset_length = len(dataset)
        print("number of samples: ", dataset_length)
        
        train_dataset = []
        test_dataset = []
        with open("train_dataset.txt", "w", encoding='utf-8') as fp1:
            with open("test_dataset.txt", "w", encoding='utf-8') as fp2:
                for i in range(dataset_length):
                    random_num = random.randint(0,dataset_length)
                    if random_num % 5 == 0:
                        test_dataset.append(dataset[i])
                        fp1.write(str(dataset[i])+'\n')
                    else:
                        train_dataset.append(dataset[i])
                        fp2.write(str(dataset[i])+'\n')
        
        train_dataset_length = len(train_dataset)
        test_dataset_length = len(test_dataset)

        print("number of training samples:", train_dataset_length)
        print("number of testing sample:", test_dataset_length)
        train_relation_dict = {}
        test_relation_dict = {}

        for x in train_dataset:
            relation = x['relation']
            if relation not in train_relation_dict:
                train_relation_dict[relation] = 1
            else:
                train_relation_dict[relation] += 1

        for x in test_dataset:
            relation = x['relation']
            if relation not in test_relation_dict:
                test_relation_dict[relation] = 1
            else:
                test_relation_dict[relation] += 1

        print("training samples relation number", train_relation_dict)
        print("testing samples relation number", test_relation_dict)
    
    def get_id_json(self):
        entityList = {}
        count = 0
        with open(self.entity_json_file_name,'r',encoding='utf-8') as fr:
            for line in fr:
                entityList[line.strip()] = count
                count +=1
        with open(self.word2id_json_file_name,'w',encoding= 'utf-8') as fw:
            json.dump(entityList,fw,ensure_ascii=False, indent = 4,separators=(',',':'))

if __name__ == '__main__':
    get_json_file = get_json_file()
    get_json_file.get_rel_json()
    get_json_file.get_dataset_json()
    get_json_file.get_word2vec_json()
    get_json_file.train_test_split()
    get_json_file.get_id_json()
    # word2vec = np.load('word2vec.npy')
    # print(word2vec.shape)
