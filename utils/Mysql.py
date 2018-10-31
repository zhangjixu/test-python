import pymysql

db = pymysql.connect(host="", port=3306, user="", passwd="", db="test", charset="utf8")
cursor = db.cursor()


class MysqlHelper(object):
    def query(self, sql):
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def save(self, sql):
        try:
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            print("insert into ecxeption : " + str(e))
            db.rollback()

    def close(self):
        db.close()
