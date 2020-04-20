import os
import thulac
import sys
import json
from pre_load import neo_con

all_entity = []
with open("result/train_data.txt","r",encoding='utf-8') as train_data:
    i = 0
    for line in train_data:
        if line =='\n':
            continue
        if i%2 == 0:
            i+=1
        else:
            i+=1
            entity = line.strip().split()
            if entity!=[]:
                for k in entity:
                    all_entity.append(k)
           
all_entity = set(all_entity)
all_entity1 = [i for i in all_entity]

with open("result/all_entity.txt",'w',encoding='utf-8') as fw:
    db = neo_con
    for entity_name in all_entity:
        # answer = db.matchSchoolItembyTitle(entity_name)
        # if answer == []:
        fw.write(entity_name+'\n')
    
