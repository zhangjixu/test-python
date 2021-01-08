from collections import namedtuple


def test_tuple():
    """
    生成器表达式
    虽然也可以用列表推导来初始化元组、数组或其他序列类型，但是生成器表达式是更好的选择。
    这是因为生成器表达式背后遵守了迭代器协 议，可以逐个地产出元素，而不是先建立一个完整的列表，
    然后再把这 个列表传递到某个构造函数里。
    Returns:

    """
    # 用生成器表达式初始化元组和数组
    symbols = '$¢£¥€¤'
    tup = tuple(ord(symbol) for symbol in symbols)
    print(tup)

    # 使用生成器表达式计算笛卡儿积
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirt)

    # 把元组用作记录
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    for country, _ in traveler_ids:
        print(country)


def test():
    tup = (1, 2)
    print(a.count(1))
    tup[2] = 3
    print(tup[0])


def test_namedtuple():
    """
    创建一个具名元组
    具名元组需要两个参数，一个是类名，另一个是类的各个 字段的名字。
    Returns:

    """
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(tokyo)
    print(tokyo._fields)


if __name__ == '__main__':
    b = 1
    a = 2
    a, b = b, a
    print(a, b)
    test()
