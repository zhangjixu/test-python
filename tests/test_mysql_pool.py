# -*- coding: UTF-8 -*-

from MysqlPool import Mysql
from Mysql import MysqlHelper

# 申请资源
mysql = Mysql()
mysqlHelper = MysqlHelper()


def query():
    sqlAll = "select * from test;"
    result = mysql.getAll(sqlAll)
    if result:
        print("get all")
        for row in result:
            print(row[0], row[1].decode(), row[2], row[3])

    # 释放资源
    mysql.dispose()


def save():
    sql = "insert into test(name, age, cdate) values('李四', 22, '2018-10-26 16:20:59')"
    # data = ["王五", 22, "2018-10-26 16:20:59"]
    mysql.insertOne(sql)


if __name__ == '__main__':
    # save = "insert into test(name, age, cdate) values('%s', %d, '%s')" % ('李四', 22, '2018-10-26 16:20:59')
    save = "insert into test(name, age, cdate) values('李四', 22, '2018-10-26 16:20:59'), ('wangwu', 20, '2018-10-26 17:20:59')"
    mysqlHelper.save(save)
    sql = "select * from test;"
    data = mysqlHelper.query(sql)
    mysqlHelper.close()
    print(data)
