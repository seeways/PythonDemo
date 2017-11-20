# 输出斐波那契数列
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


# 输出斐波那契数组
def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


if __name__ == '__main__':
    import sys

    num = int(sys.argv[1])
    if num >= 50:
        fib(num)
    else:
        print(fib2(num))
