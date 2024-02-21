# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        return n

    n = getdata()
    dp = [0] * (n+1)
    if n%2 != 0 :
        print(0)
    else :
        if n == 0 :
            print(0)
        elif n == 2:
            print(3)
        elif n == 4 :
            print(11)
        else :
            dp[0] = 1
            dp[2] = 3
            dp[4] = 11
            for i in range(6, n+1, 2) :
                for j in range(0,i-1,2) :
                    dp[i] += dp[j]*2
                dp[i] += dp[i-2]
            print(dp[n])

