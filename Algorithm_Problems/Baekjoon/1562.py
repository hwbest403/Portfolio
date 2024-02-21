# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        return n

    n = getdata()
    dp=list(0 for _ in range(101))
    dp[10] = 1
    # dp[10] -> 9876543210 (9, 0)
    # dp[11] -> 8+dp[10], dp[10]+1 (8, 0) (9, 1)
    # dp[12] ->
    # dp[i] -> dp[i-1]