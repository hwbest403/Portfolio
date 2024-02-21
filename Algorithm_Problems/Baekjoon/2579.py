# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        score = list()
        for i in range(n) :
            score.append(int(input()))
        return n, score

    n, score = getdata()
    dp = list(0 for _ in range(n))
    if n == 1:
        print(score[0])
    elif n == 2:
        print(score[0]+score[1])
    else :
        dp[0] = score[0]
        dp[1] = score[0]+score[1]
        dp[2] = max(score[0],score[1])+score[2]
        for i in range(3,n) :
            dp[i] = max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i])
        print(dp)