# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def printboard(board) :
        for row in board :
            print(row)

    def maxboard(board) :
        res = 0
        for row in board :
            if res < max(row) :
                res = max(row)
        return res

    def getdata():
        n, m = map(int,input().split())
        board = list(list(map(int, input().split())) for _ in range(n))
        return n, m, board

    n, m, board = getdata()
    dp = list(list(0 for _ in range(m+1)) for _ in range(n+1))
    for i in range(1,n+1) :
        for j in range(1,m+1) :
            if board[i-1][j-1] == 0:
                tmp = 10**6
                tmp = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1],tmp)
                if tmp == 10**6 :
                    tmp = 0
                dp[i][j] = tmp+1
    # printboard(dp)
    print(maxboard(dp))