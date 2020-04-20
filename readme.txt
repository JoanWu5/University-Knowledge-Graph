安装neo4j
将neo4jimport文件夹中的文件导入neo4j目录下的import中，执行如下操作：

neo4j数据导入全操作：
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

到demo目录下的manage.py目录下，运行python manage.py runserver 0.0.0.0:8000即可得到网站


对于相关实体爬取，请见dfs_tree_crawler
对于实体命名识别，请见NER
对于属性抽取，请见SchoolCrawler
对于实体分类，请见label_data和KNN_predict
对于关系抽取，爬取部分请见wikidataSpider, 请见Relation Extraction