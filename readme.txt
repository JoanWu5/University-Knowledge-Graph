neo4j���ݵ���ȫ������
LOAD CSV WITH HEADERS  FROM "file:///school_pedia.csv" AS line  
CREATE (p:SchoolItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList}) 

CREATE CONSTRAINT ON (c:SchoolItem)
ASSERT c.title IS UNIQUE

// �����µĽڵ�
LOAD CSV WITH HEADERS FROM "file:///new_node.csv" AS line
CREATE (:NewNode { title: line.title })

//�������
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

ɾ������neo4j���ݣ�MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r 