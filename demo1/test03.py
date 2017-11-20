import re


def test(filename, num=1):
    # 'Find Top Frequent Words:'
    fp = open(filename, 'r')
    text = fp.read()
    fp.close()

    lst = re.split('[0-9\W]+', text)

    # create words set, no repeat
    words = set(lst)
    d = {}
    for word in words:
        d[word] = lst.count(word)
    del d['']

    result = []
    for key, value in sorted(d.iteritems(), key=lambda k_v: (k_v[1], k_v[0]), reverse=True):
        result.append((key, value))
    return result[:num]


if __name__ == '__main__':
    # readlines与xreadlines区别
    test('./'
         '2.txt', 10)
    # f = open("2.txt")
    # f.close()
    # print(f.readlines())
    # print(f.xreadlines())
