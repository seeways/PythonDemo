birth = 0
temp = input('birth: ')


def m_global():
    global birth
    global temp
    while not temp.isdigit():
        if not temp.isdigit():
            birth = 0
            temp = input("抱歉，您的输入有误，请输入一个整数：")
    else:
        birth = int(temp)


if __name__ == '__main__':
    m_global()
    if birth < 2000:
        print('00前')
    else:
        print('00后')
