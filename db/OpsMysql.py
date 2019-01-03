# @Author: zhangjixu
# @Time: 2018/11/6 2:16 PM
# @FileName: OpsMysql.py
# @Description:
# @Version: 1.0.0

from db.MySQLUtils import MySQLUtils
from db import cfg


class OpsMysql(object):


    '''
    用于操作 mysql 数据库
    '''

    def query(self, sql, value=None):
        '''
        用于执行查询语句
        Args:
            sql: 执行的 sql 语句
            value: 语句中的参数列表

        Returns:

        '''
        with MySQLUtils(host=cfg.MYSQL_ALPHACASH_HOST, port=cfg.MYSQL_ALPHACASH_PORT,
                        user=cfg.MYSQL_ALPHACASH_ADMIN_USER, password=cfg.MYSQL_ALPHACASH_ADMIN_PWD,
                        database=cfg.MYSQL_ALPHACASH_DB) as cnx:
            cur = cnx.cursor(dictionary=True)
            cur.execute(sql, value)
            return cur.fetchall()

    def save(self, sql, value=None):
        '''
        执行 增 删 改 语句
        Args:
            sql: 执行的 sql 语句
            value: 语句中的参数列表

        Returns:

        '''
        with MySQLUtils(host=cfg.MYSQL_ALPHACASH_HOST, port=cfg.MYSQL_ALPHACASH_PORT,
                        user=cfg.MYSQL_ALPHACASH_ADMIN_USER, password=cfg.MYSQL_ALPHACASH_ADMIN_PWD,
                        database=cfg.MYSQL_ALPHACASH_DB) as cnx:
            cur = cnx.cursor(dictionary=True)
            cur.execute(sql, value)
            cnx.commit()
