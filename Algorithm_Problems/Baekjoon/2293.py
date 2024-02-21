# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n, k = map(int,input().split())
        board = list(int(input()) for _ in range(n))
        return n, k, board

    n,k,board = getdata()
    dp = list(0 for _ in range(k+1))
    for c in board :
        print(f"=={c}")
        if k<c :
            continue
        dp[c] += 1
        for i in range(k+1) :
            if 0<=i-c :
                print(f"-{i}")
                dp[i] += dp[i-c]
                print(dp)
    print(dp[k])