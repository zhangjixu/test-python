#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logger import log


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


if __name__ == '__main__':
    log.info('张三')
    # 这是一个注释
    '''
    这是一个多行注释
    '''
    """
    这是一个多行注释
    """
    # json = {'a': 1, 'b': None}
    # print(json['b'] == None)
    # print('python 字符串拼接:' + '%s %s' %('ss', 12))
