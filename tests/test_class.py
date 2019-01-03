#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logger import log
import re
import random
from utils import MySQLUtils
from db.OpsMysql import OpsMysql
from tests.Student import Student
import sys

row = 3


def f1(a, b):
    """

    Args:
        a (list[int]):
        b (str):

    Returns:

    """
    pass


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


def args(name, age):
    print(name)
    print(age)


def exce():
    # raise ValueError('pool_size must >= 0')
    pass


def genera():
    for i in range(2):
        yield i
        print(' ============== ' + str(i))
    return 'ooo'


def outer(k):
    def inner(x):
        return k * x + 5

    return inner


def out(fun):
    def inner():
        print(fun.__name__)
        fun()
        return 'sss'

    return inner


@out
def mk():
    print('success')


if __name__ == '__main__':
    stu = Student('s', 19)