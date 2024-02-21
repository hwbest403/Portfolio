# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        return n

    n = getdata()
    res = 0
    i = 1
    while res<=n :
        res += i
        i += 1
    print(i-2)