from array import array
from random import random


def test1():
    """
    使用数组进行操作
    Returns:

    """
    # 利用一个可迭代对象来建立一个双精度浮点数组（类型码是 'd'）， 这里我们用的可迭代对象是一个生成器表达式。
    floats = array('d', (random() for i in range(10 ** 7)))
    # 查看数组的最后一个元素。
    print(floats[-1])

    fp = open('floats.bin', 'wb')
    # 把数组存入一个二进制文件里
    floats.tofile(fp)
    fp.close()

    # 新建一个双精度浮点空数组
    floats2 = array('d')
    fp = open('floats.bin', 'rb')
    # 把 1000 万个浮点数从二进制文件里读取出来
    floats2.fromfile(fp, 10 ** 7)
    fp.close()

    print(floats2[-1])
    print(floats2 == floats)


def test_mem():
    """
    内存视图
    Returns:

    """
    # 利用含有 5 个短整型有符号整数的数组（类型码是 'h'）创建一个 memoryview
    numbers = array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(len(memv), memv[0])

    #  创建一个 memv_oct，这一次是把 memv 里的内容转换成 'B' 类型， 也就是无符号字符
    memv_oct = memv.cast('B')
    #  以列表的形式查看 memv_oct 的内容
    print(memv_oct.tolist())

    memv_oct[5] = 4
    #  因为我们把占 2 个字节的整数的高位字节改成了4，所以这个有符号 整数的值就变成了 1024
    print(numbers)


if __name__ == '__main__':
    test_mem()
