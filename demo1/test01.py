from functools import reduce

if __name__ == '__main__':
    # 一行代码实现对列表a中的偶数位置的元素进行加3后求和？
    a = [1, 2, 3, 4, 5]
    print(reduce(lambda x, y: x + y, [a[x] + (x + 1) % 2 * 3 for x in range(0, 5)]))
