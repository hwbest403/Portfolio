# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    import math

    n = int(input())

    def primels(n, m):
        prime = list(True for _ in range(n + 1))
        for i in range(2, int(math.sqrt(n)) + 1):
            if prime[i] == True:
                for j in range(i+i,n,i) :
                    prime[j] = False
        return [i for i in range(2, n) if prime[i] == True and m%i == 0]

    if n>10**6 :
        ls = primels(10**6, n)
    else :
        ls = primels(n, n)

    def sol(ls, n) :
        result = n
        for p in ls :
            while n%p==0 :
                n //= p
            result = result/p*(p-1)
        if n != 1 :
            result = result/n*(n-1)
        return int(result)

    print(sol(ls, n))