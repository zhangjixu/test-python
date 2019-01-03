import pymongo
from db.OpsMysql import OpsMysql


client = pymongo.MongoClient(host='192.168.16.198', port=27017)
mysql = OpsMysql()
# 指定数据库
db = client['test']

if __name__ == '__main__':
    docs = []
    collection = db.stu
    for i in range(1, 5):
        doc = {'i': i}
        docs.append(doc)
        print(len(docs))

    collection.insert_many(docs)
