LOAD CSV WITH HEADERS  FROM "file:///school_pedia.csv" AS line  
CREATE (p:SchoolItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList}) 
ɾ������neo4j���ݣ�MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r 
CREATE CONSTRAINT ON (c:SchoolItem)
ASSERT c.title IS UNIQUE