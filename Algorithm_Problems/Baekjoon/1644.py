# coding = utf-8

import sys
import math
input = sys.stdin.readline

def isprime(a) :
    for i in range(2, math.ceil(math.sqrt(a))+1) :
        if a%i == 0 :
            return False
    return True

def getprime(n) :
    a = [False, False] + [True]*(n-1)
    primes=list()
    for i in range(2,n+1) :
        if a[i] :
            primes.append(i)
            for j in range(2*i,n+1,i) :
                a[j] = False
    return primes

n = int(input())
if n == 1 :
    print(0)
    sys.exit()
primes = getprime(n)

left, right = 0, 0
res = 0
tmp = primes[left]
while left < len(primes):
    if tmp < n :
        right += 1
        if right == len(primes) :
            break
        tmp += primes[right]
    elif tmp > n :
        left += 1
        tmp -= primes[left-1]
    else :
        res += 1
        left += 1
        tmp -= primes[left-1]
print(res)