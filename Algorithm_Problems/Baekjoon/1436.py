if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    n = int(input())
    cnt, num = 0, 0
    while True :
        num += 1
        if '666' in str(num) :
            cnt += 1
        if cnt == n :
            print(num)
            break