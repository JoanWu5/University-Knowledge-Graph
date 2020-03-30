

# 说明

> 本项目为一些用于获取知识图谱中三元组关系的python脚本。包括爬取Wikidata数据的爬虫、提取所有中文维基页面的脚本以及将Wikidata三元组数据对齐到中文维基页面语句的脚本。

### 运行环境

python3、 Scrapy、neo4j(仅对齐时需要)、MongoDB(标注关系数据集时需要)



> 注意：下面所有爬虫执行命令scrapy crawl XXX 请在各个模块的根目录执行，否则可能由于路径问题找不到文件导致程序报错


### wikidataCrawler

**用来爬取wikidata上定义的所有关系**

wikidata中的所有关系都汇总在该网页上[(链接)](https://www.wikidata.org/wiki/Wikidata:List_of_properties/Summary_table) ，wikidataCrawler将该网页下的汇总的所有关系及其对应的中文名称爬取下来，存储为json格式

![](https://raw.githubusercontent.com/CrisJk/SomePicture/master/blog_picture/wikiRelationSumary.png)

##### 使用方法

进入到wikidataCrawler目录下，运行`scrapy crawl relation`即可爬取wikidata中定义的所有关系。可以得到`relation.json`和`chrmention.json`。

* `relation.json`内容: 关系的id，关系所属的大类，关系所属子类，对应的链接，关系的英文表示
* `chrmention.json`内容: 关系的id，关系的中文表示（对于不包含中文表示的数据暂时不做处理）。



将`relation.json`和`chrmention.json`的数据进行合并，运行`mergeChrmentionToRelation.ipynb`即可，得到的结果存储在`result.json`中，匹配失败的存在`fail.json` 中

### wikientities

**用来爬取实体，返回json格式**

进入到wikientities目录下，运行`scrapy crawl entity`。可以得到 `entity.json`。

`entity.json` 是以predict_labels.txt中的实体为搜索词，在wikidata上搜索返回的json内容。

`entity.json`中还包括搜索词(即实体)以及实体所属的类别(和predict_labels.txt中一样)也加入json中存储。

> 由于我目前想做一个农业领域的知识图谱，因此predict_label.txt中很多词都是关于农业的，若想爬取其他实体，则自己修改predict_label.txt中的数据即可。

### wikidataRelation说明

##### 用来爬取实体和实体间的关系三元组，返回三元组

Wikidata是一个开放的全领域的知识库，其中包含大量的实体以及实体间的关系。下图是一个wikidata的实体页面

![](https://raw.githubusercontent.com/CrisJk/SomePicture/master/blog_picture/wikidataPage.png)



从图中可以看到wikidata实体页面包含实体的描述和与该实体相关联的其它实体及对应的关系。

##### 使用方法

首先运行preProcess.py，得到readytoCrawl.json。然后进入到wikidataRelation目录下，运行scrapy crawl entityRelation。可以得到`entityRelation.json` 。

`entityRelation.json`是利用`entity.json`中的所有实体为基础，获取与这些实体相关的其他实体和关系。

### wikidataProcessing 

##### 用来处理得到的三元组关系(entityRelation.json)

将得到的entityRelation.json 处理成csv，并且存入neo4j数据库。该文件夹下的两个文件`school_pedia.csv　`和`school_pedia1.csv` 是爬取互动百科相关页面得到的，对应的就是wikientities目录下的`predict_label.txt`中的实体。运行`relationDataProcessing.py` 可以得到`new_node.csv` (即从wikidata实体页面中爬取得到的实体不包含在`predict_label.txt`中的部分)、`wikidata_relation.csv`(predict_label.txt中实体之间的关系)以及`wikidata_relation2.csv`(predict_label.txt中实体和新发现实体间的关系)，将该目录下所有csv导入到neo4j中，具体操作参见[SchoolKnowledgeGraph](https://github.com/JoanWu5/University-Knowledge-Graph) 中的项目部署部分。



### wikidataAnalyse

wikidataAnalyse: 得到staticResult.txt,统计各种关系的分布情况

extractEntityAttribute: 获取实体属性得到attributes.csv




