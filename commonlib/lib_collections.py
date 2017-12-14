#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/14 0014.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# collections是Python内建的一个集合模块，提供了许多有用的集合类。
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# nametuple(tuple)
point = namedtuple("point", ['x', 'y'])
p = point(1, 2)
print(p.x, p.y)

# nametuple 看名字应该也是属于tuple的子类
print(isinstance(p, point))
print(isinstance(p, tuple))

print("-------------------")
# deque 一种类似列表的序列，用于在其端点附近访问数据
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('x')  # 从右边添加一个元素
q.appendleft('y')  # 从左边添加一个元素
print(q)  # deque(['y', 'a', 'b', 'c', 'x'])
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
print("-------------------")

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
dd = defaultdict(lambda: "no value")
dd['key1'] = "abc"
print(dd['key1'])  # abc
print(dd['key2'])  # no value

print("-------------------")
# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict
# Dictionary that remembers insertion order记住插入顺序的字典
d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
print(d)  # {'a': 1, 'b': 2, 'c': 3}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
print(od)


# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class FIFO(OrderedDict):
    """docstring for FIFO：last update ordered dict"""
    def __init__(self, capacity):
        super(FIFO, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containKey = 1 if key in self else 0
        if len(self) - containKey >= self._capacity:
            last = self.popitem(last=False)
            print("remove:", last)
        if containKey:
            del self[key]
            print("set:", (key, value))
        else:
            print("add:", (key, value))
        OrderedDict.__setitem__(self, key, value)


print("-------------------")
# counter 计数器
# Counter实际上也是dict的一个子类，下面的代码中重复的都去掉了
c = Counter()
for ch in "programming":
    c[ch] += 1
print(c)  # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
