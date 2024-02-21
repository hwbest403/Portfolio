# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    MOD = 1000000007
    facto = list(1 for _ in range(4000001))

    for i in range(1, 4000001) :
        facto[i] = (facto[i-1]*i)%MOD

    m = int(input())
    for _ in range(m) :
        n, k = map(int,input().split())
        a = facto[n]
        inv_b = (facto[n-k]*facto[k]) % MOD

        b = 1
        e = MOD-2
        while e :
            if e%2 :
                b = (inv_b * b) % MOD
            inv_b = (inv_b*inv_b) % MOD
            e //= 2
        print((a*b)%MOD)