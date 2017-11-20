if __name__ == '__main__':
    num = 10
    temp = 0
    for n in range(num):
        temp = num/(n+1)
        print((" " * int(temp))+("*" * n)+(" " * int(temp)))
