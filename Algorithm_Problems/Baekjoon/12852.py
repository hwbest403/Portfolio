# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    n = int(input())
    dp = [10**6] *(n+1)
    cal = [2] *(n+1)
    # //2 -> 0 //3 -> 1 -1 -> 2
    for i in range(n+1) :
        min1, min2, min3 = 10**6, 10**6, 10**6
        if i==0 :
            dp[i] = 0
        elif i==1 :
            dp[i] = 0
        else :
            if i%2==0 :
                min1 = dp[i//2]
            if i%3==0 :
                min2 = dp[i//3]
            min3 = dp[i-1]
            dp[i] = min(min1,min2,min3) + 1
            if dp[i]-1 == min1 :
                cal[i] = 0
            elif dp[i]-1 == min2 :
                cal[i] = 1
            else :
                cal[i] = 2

    print(dp[n])
    while n!=1 :
        print(n, end = " ")
        if cal[n] == 0 :
            n=n//2
        elif cal[n] == 1:
            n=n//3
        else :
            n-=1
    print(1)