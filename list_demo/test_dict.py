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


if __name__ == '__main__':
    test1()
