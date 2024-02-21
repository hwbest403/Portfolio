# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        return n

    coin = [500, 100, 50, 10, 5, 1]
    n = getdata()
    ret = 1000 - n
    res = 0
    for c in coin :
        # print(f"=={c}")
        while ret >= c :
            ret -= c
            res += 1
        # print(ret, res)
    print(res)