import pymongo
import time
from bson.objectid import ObjectId
from db.OpsMysql import OpsMysql

DATETIME_FORMAT = '%Y%m%d %H:%M'

client = pymongo.MongoClient(host='10.76.88.22', port=26301)
mysql = OpsMysql()
# 指定数据库
db = client['model']


def query(json):
    # 指定 collection
    collection = db.model_result
    result = collection.find(json)
    # result 是个 cursor
    return result


def query_by_ts(json):
    # 指定 collection
    collection = db.model_result
    # myquery = {"ut": {"$gte": start_ts, "$lt": end_ts}}
    result = collection.count_documents(json)
    print(result)


# 字符串转时间戳
def parse_str(date):
    t = time.strptime(date, DATETIME_FORMAT)
    return int(round(time.mktime(t) * 1000))


# 判断 document 中是否包含这些字段
def is_exist(json):
    flag = False
    arr = ['sin_id', 'model_id']
    model_result_arr = ['level', 'segment', 'status_code', 'default_proba']
    for string in arr:
        if string in json:
            flag = True
            return flag

    if 'model_result' in json:
        model_result = json['model_result']
        for string in model_result_arr:
            if string in model_result:
                flag = True
                return flag

    return flag


if __name__ == '__main__':
    start_ts = time.time()
    json = {"ut": {"$gte": parse_str('20180115 18:00'), "$lt": parse_str('20180115 19:00')}}
    # json = {"_id": ObjectId("5a02d557f0a22e84bc0d9542")}
    # query_by_ts(json)
    result = query(json)
    for document in result:
        try:
            _id = document['_id']
            ut = document['ut']
            org = 'ac'
            sql_key = 'insert into `model_result`(`_id`,`ut`,`org_id`,'
            sql_values = " ) values('" + str(_id) + "'," + str(ut) + ",'" + str(org) + "'"
            if is_exist(document):
                arr = ['sin_id', 'model_id']
                for string in arr:
                    if string in document and document[string] != None:
                        value = document[string]
                        if string == 'sin_id':
                            sql_key += '`order_id`,'
                        else:
                            sql_key += "`" + string + "`,"
                        sql_values += ", '" + str(value) + "' "

                if 'model_result' in document and document['model_result'] != None:
                    model_result = document['model_result']
                    model_result_arr = ['level', 'segment', 'status_code', 'default_proba']
                    for string in model_result_arr:
                        if string in model_result and model_result[string] != None:
                            value = model_result[string]
                            if string == 'level':
                                sql_key += '`lv`,'
                                if type(value) is int:
                                    value = value / 10.0
                                sql_values += "," + str(value) + ""
                            else:
                                sql_key += "`" + string + "`,"
                                sql_values += ", '" + str(value) + "' "
        except Exception as e:
            print('parse document exception : ' + e)
            continue
        sql = sql_key[0:len(sql_key) - 1] + sql_values + ")"
        print(sql)
        # mysql.save(sql)

    end_ts = time.time() - start_ts
    print("cost time : " + str(end_ts) + " ms")
