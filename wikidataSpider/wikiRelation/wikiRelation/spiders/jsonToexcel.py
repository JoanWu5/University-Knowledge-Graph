import csv
import json


def trans(jsonpath, csvpath):
    # json_file = open(jsonpath, 'r', encoding='utf8')
    csv_file = open(csvpath, 'w', newline='',encoding='utf-8')
    keys = []
    writer = csv.writer(csv_file)

    with open(jsonpath, 'r', encoding='utf8') as json_file:
        dic_data = [json.loads(line) for line in json_file]
    # dic_data = json.loads(json_data, encoding='utf8')

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


if __name__ == '__main__':
    trans('entityRelation_zh.json', 'entityRelation.csv')
