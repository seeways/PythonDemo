from random import shuffle

if __name__ == '__main__':
    # 将列表a的元素顺序打乱，再对a进行排序得到列表b，然后把a和b按元素顺序构造一个字典d。
    a = [1, 2, 3, 4, 5]
    # 将列表a的元素顺序打乱
    shuffle(a)

    # 再对a进行排序得到列表b
    b = sorted(a, reverse=True)

    # 然后把a和b按元素顺序构造一个字典d。
    d = dict(zip(a, b))

    print(d)



