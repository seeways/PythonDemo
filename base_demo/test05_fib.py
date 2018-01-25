# 输出斐波那契数列
import sys


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
    """
    sys.argv 是从外部获取参数，不要盲目运行，否则会报越界异常
    
    sys.argv[0] 是文件本身，是没有任何输出的
    
    sys.argv[1] 则输出数据本身
    
    本例用法：
    1. 打开命令行并切换到本目录下
    2. python test05_fib.py 数据(如 python test05_fib.py 123)
    3. 得到fib数列 1 1 2 3 5 8 13 21 34 55 89
    """
    num = int(sys.argv[1])
    if num >= 50:
        fib(num)
    else:
        print(fib2(num))