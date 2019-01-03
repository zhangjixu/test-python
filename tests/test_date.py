import time

DATETIME_FORMAT = '%Y%m%d'


# 字符串转时间戳
def parse_str(date):
    t = time.strptime(date, DATETIME_FORMAT)
    return int(round(time.mktime(t) * 1000))


# 时间戳转字符串
def ts_str(ts):
    st = time.localtime(ts)
    return time.strftime('%Y-%m-%d %H:%M:%S', st)


if __name__ == '__main__':
    print()
    print(parse_str('20180901'))
    print(ts_str(1536422400))
    print(round(23.23, 1))
    print(round(23.67))
