# coding = utf-8

if __name__ == '__main__':
    import sys
    from itertools import *
    input = sys.stdin.readline

    def getdata():
        n, l, r = map(int,input().split())
        return n, l, r

    def printdp(dp) :
        for idx, row in enumerate(dp) :
            if idx == 0 :
                continue
            print(f"=={idx}th==")
            for i in row :
                print(i)

    n, l, r = getdata()
    dp=list(list(list(0 for _ in range(i+1)) for _ in range(i+1)) for i in range(n+1))
    # n == 1
    # 1 총 : 1
    # n == 2
    # 0 1
    # 1 0 총 : 2
    # n == 3
    # 0 1 1
    # 1 2 0 dp[2][2] = 2C1
    # 1 0 0 총 : 6
    # n == 4
    # 0 2 3 1
    # 2 6 3 0
    # 3 3 0 0
    # 1 0 0 0 총 : 24
    # n == 5
    # 0  6  11 6 1
    # 6  24 18 3 0
    # 11 18 6  0 0 dp[3][3] = 4C2
    # 6  3  0  0 0
    # 1  0  0  0 0 총 : 120
    for case in permutations([i+1 for i in range(3)], 3) :
        print(case)
    printdp(dp)