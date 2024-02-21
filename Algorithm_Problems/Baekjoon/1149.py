# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(list(map(int, input().split())) for _ in range(n))
        return n, board

    n, board = getdata()
    # dp[n][0,1,2] -> dp[n][0]은 0의 색으로 끝나는 n까지 최소
    # dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + board[i][0]
    dp = list(list(0 for _ in range(3)) for _ in range(n))
    dp[0] = board[0]
    for i in range(1,n) :
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + board[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + board[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + board[i][2]
    for row in dp :
        print(row)
    print(min(dp[n-1]))