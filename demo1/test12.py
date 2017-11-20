# -*- coding: utf-8 -*-
import math


def my_abs(arg_name_is_x):
    arg_name_is_x = int(arg_name_is_x)
    if not isinstance(arg_name_is_x, (int, float)):
        raise TypeError("类型错误，请输入数字!")
    if arg_name_is_x > 0:
        print(arg_name_is_x)
    else:
        print(-arg_name_is_x)


# 返回多个值(元组)
# 参数为坐标，位移，角度
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


is_stop = True

if __name__ == '__main__':
    # 打印元组
    print(move(100, 100, 100, 90))
    # abs测试
    x = input("absNum:")
    my_abs(x)
    while is_stop:
        stop_controller = input("isStop? \nYes:1 No:0\n")
        if int(stop_controller) == 1:
            is_stop = True
            x = input("absNum:")
            my_abs(x)
        elif int(stop_controller) == 0:
            is_stop = False
        else:
            stop_controller = input("you not type 0 or 1! \nYes:1 No:0\n")
            is_stop = True


