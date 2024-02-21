# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(map(int, input().split()))
        return n, board

    # dp[i] -> i까지 LIS
    # 초기화 dp -> 1 for all
    # dp[0] = 1 자기 자신은 크기 1의 LIS
    # dp[1] = if board[1]>board[0] : max(dp[1], dp[0]+1)
    # dp[2] = 0부터 1까지 if board[2] > board[i] :
    # max(dp[i]+1, dp[2])
    # ....
    def sol(board, dp) :
        for right in range(n) :
            for left in range(right) :
                if board[right] > board[left] :
                    dp[right] = max(dp[left]+1, dp[right])
        return dp

    n, board = getdata()
    dp = list(1 for _ in range(n))

    sol(board,dp)
    print(max(dp))