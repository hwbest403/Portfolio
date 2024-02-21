# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n, k = map(int,input().split())
        return n, k

    def printdp(dp) :
        for row in dp :
            print(row)

    n, k = getdata()
    dp=list(list(0 for _ in range(n+1)) for _ in range(k+1))
    for i in range(n+1) :
        dp[1][i] = 1
    for i in range(1, k+1) :
        dp[i][0] = 1
    # dp[k][n],
    for i in range(2, k+1) :
        for j in range(1, n+1) :
            for l in range(j+1) :
                dp[i][j] += dp[i-1][l]
    print(dp[-1][-1]%1000000000)