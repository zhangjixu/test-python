import pymongo
from bson.objectid import ObjectId
from utils.MongoUtils import MongoUtils


def query():
    client = pymongo.MongoClient(host='10.76.2.3:27017,10.76.2.4:27017')
    # 指定数据库
    db = client['transfer_rpt']
    collection = db.rpt_contacts
    document = {'_id': ObjectId('576a1d7118ca471eb0195224')}
    cursor = collection.find(document)
    for doc in cursor:
        print(doc)

    cursor.close()


def query_1():
    collection = MongoUtils('192.168.16.198:27017', 'test', 'user').getMongo()
    document = {'_id': ObjectId('5bebe7e1d953ca91c44c3b84')}
    cursor = collection.find(document)
    for doc in cursor:
        print(doc['_id'])
        print(doc['name']['class']['name'])

    cursor.close()


def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    return i * 2


if __name__ == '__main__':
    query_1()
