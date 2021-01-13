import collections
from types import MappingProxyType
from dis import dis


def test():
    """
    元组的话，只有当一个元组包含的所有元素 都是可散列类型的情况下，它才是可散列的。
    Returns:

    """
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    print(a == b == c == d == e)


def test1():
    """
    字典推导
    Returns:

    """
    DIAL_CODES = [(86, 'China'), (91, 'India'), (1, 'United States')]
    #  这里把配好对的数据左右换了下，国家名是键，区域码是值。
    country_code = {country: code for code, country in DIAL_CODES}
    print(country_code)

    # 跟上面相反，用区域码作为键，国家名称转换为大写，并且过滤掉 区域码大于或等于 66 的地区。
    dic = {code: country.upper() for country, code in country_code.items() if code < 66}
    print(dic)


def test2():
    """
    字典变种
    Returns:

    """
    # 这个映射类型会给键准备一个整数计数器。每次更新一个键的时候 都会增加这个计数器
    ct = collections.Counter('abracadabra')
    print(ct)

    ct.update('aaaaazzz')
    print(ct)

    # most_common([n]) 会按照次 序返回映射里最常见的 n 个键和它们的计数
    print(ct.most_common(2))


def test3():
    """
    不可变映射类型
    Returns:

    """
    d = {1: 'A'}
    #  d 中的内容可以通过 d_proxy 看到。
    d_proxy = MappingProxyType(d)
    print(d_proxy)

    # 会报错
    # 通过 d_proxy 并不能做任何修改。
    # d_proxy[2] = 'x'

    # d_proxy 是动态的，也就是说对 d 所做的任何改动都会反馈到它上 面。
    d[2] = 'B'
    print(d_proxy)


if __name__ == '__main__':
    test3()
    dis('{1}')
    print(test3.__doc__)
