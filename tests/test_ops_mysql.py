# @Author: zhangjixu
# @Time: 2018/11/6 2:27 PM
# @FileName: test_ops_mysql.py
# @Description:
# @Version: 1.0.0

from db.OpsMysql import OpsMysql

if __name__ == '__main__':
    ops_mysql = OpsMysql()
    # ops_mysql.save('''insert into test(name, age) values(%s, %s)''', ('李四', 20))
    # ops_mysql.save('''update test set name = %s where id = %s''', ('李四', 17))
    data = ops_mysql.query('''select * from test  where `id` = %s''', (58,))
    # 字典形式传递参数
    # data = ops_mysql.query('''select * from test  where `id` = %(id)s''', {'id': 17})
    for row in data:
        print(row['id'])
