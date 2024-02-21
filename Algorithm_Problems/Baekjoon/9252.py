# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        a = input().rstrip()
        b = input().rstrip()
        return a, b

    a, b = getdata()
    dp = list(list(0 for _ in range(len(b)+1)) for _ in range(len(a)+1))
    result=list()
    for i in range(1, len(a)+1) :
        for j in range(1, len(b)+1) :
            if a[i-1] == b[j-1] :
                dp[i][j] = dp[i-1][j-1] + 1
                result.append(a[i-1])
            else :
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp[-1][-1])
    x = len(a)
    y = len(b)
    ans = list()
    while x > 0 and y > 0:
        if dp[x][y - 1] == dp[x][y]:
            y -= 1
        elif dp[x - 1][y] == dp[x][y]:
            x -= 1
        else:
            ans.append(b[y-1])
            x -= 1
            y -= 1
    ans = ans[::-1]
    for i in range(len(ans)):
        print(ans[i], end="")