def test_list():
    """
    列表推导可以帮助我们把一个序列或是其他可迭代类型中的元素过滤或是加工，然后再新建一个列表
    Returns:

    """
    x = 'ABC'
    dummy = [ord(x) for x in x]
    print(dummy)

    # 使用列表推导式加过滤条件
    symbols = '$¢£¥€¤'
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    print(beyond_ascii)

    # 笛卡尔积
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)


def test():
    """
    在平行赋值中，* 前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的任意位置
    Returns:

    """
    a, b, *rest = range(5)
    print(a, b, rest)
    a, b, *rest = range(3)
    print(a, b, rest)
    a, b, *rest = range(2)
    print(a, b, rest)
    a, *body, c, d = range(5)
    print(a, body, c, d)


def test_split():
    """
    切片取值
    Returns:

    """
    s = 'bicycle'
    a = s[::3]
    print(a)
    print(s[::-1])


def test_sort():
    """
    列表排序
    Returns:

    """
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    #  新建了一个按照字母排序的字符串列表。 原列表并没有变化
    print(sorted(fruits))

    #  按照字母降序排序
    print(sorted(fruits, reverse=True))

    # 按照长度排序
    print(sorted(fruits, key=len))

    # 按照长度降序排序的结果
    print(sorted(fruits, key=len, reverse=True))

    fruits.sort()

    # 此时 fruits 本身被排序。
    print(fruits)


def test2():
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(fruits[::-1])
    print(sorted(fruits, key=lambda word: word[::-1]))


def test3():
    list1 = [1, 2]
    list2 = list(list1)
    print(list2)


if __name__ == '__main__':
    test3()
    print(test2.__defaults__)
