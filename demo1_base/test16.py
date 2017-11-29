# 递归阶乘  超过栈容易溢出
def recursive(n):
    if n == 1:
        return 1
    return n * recursive(n - 1)


# 尾递归 优化，末尾调用时函数调用前运算，可以始终调用一个栈,简直就是扯淡
def optimize(n, product):
    if n == 1:
        return product
    return optimize(n - 1, n * product)


# 循环测试
def for_test(ns):
    temp = 1
    for n in range(1, ns+1):
        temp *= n
    return temp


if __name__ == '__main__':
    print(recursive(100))

    # print(optimize(500, 1000))
    # print(optimize(4, 5))
    # print(optimize(3, 20))
    # print(optimize(2, 60))
    # print(optimize(1, 120))
    print(for_test(100))
