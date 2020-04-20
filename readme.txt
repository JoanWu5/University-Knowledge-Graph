��װneo4j
��neo4jimport�ļ����е��ļ�����neo4jĿ¼�µ�import�У�ִ�����²�����

neo4j���ݵ���ȫ������
LOAD CSV WITH HEADERS  FROM "file:///school_pedia.csv" AS line  
CREATE (p:SchoolItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList}) 

CREATE CONSTRAINT ON (c:SchoolItem)
ASSERT c.title IS UNIQUE


LOAD CSV WITH HEADERS FROM "file:///new_node.csv" AS line
CREATE (:NewNode { title: line.title })


CREATE CONSTRAINT ON (c:NewNode)
ASSERT c.title IS UNIQUE

LOAD CSV  WITH HEADERS FROM "file:///wikidata_relation2.csv" AS line
MATCH (entity1:SchoolItem{title:line.SchoolItem}) , (entity2:NewNode{title:line.NewNode})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)

LOAD CSV  WITH HEADERS FROM "file:///wikidata_relation.csv" AS line
MATCH (entity1:SchoolItem{title:line.SchoolItem1}) , (entity2:SchoolItem{title:line.SchoolItem2})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)


LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:SchoolItem{title:line.Entity}), (entity2:SchoolItem{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2);
                                                            
LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:SchoolItem{title:line.Entity}), (entity2:NewNode{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2);
                                                            
LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:NewNode{title:line.Entity}), (entity2:NewNode{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2);
                                                            
LOAD CSV WITH HEADERS FROM "file:///attributes.csv" AS line
MATCH (entity1:NewNode{title:line.Entity}), (entity2:SchoolItem{title:line.Attribute})
CREATE (entity1)-[:RELATION { type: line.AttributeName }]->(entity2)  

��demoĿ¼�µ�manage.pyĿ¼�£�����python manage.py runserver 0.0.0.0:8000���ɵõ���վ


�������ʵ����ȡ�����dfs_tree_crawler
����ʵ������ʶ�����NER
�������Գ�ȡ�����SchoolCrawler
����ʵ����࣬���label_data��KNN_predict
���ڹ�ϵ��ȡ����ȡ�������wikidataSpider, ���Relation Extraction