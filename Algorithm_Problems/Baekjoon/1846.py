# coding = utf-8

import sys
input = sys.stdin.readline

n = int(input())

def sol() :
    if n == 3:
        print(-1)
    elif n%2 == 1 :
        for i in range(2, n-1) :
            print(i)
        print(1)
        print(n)
        print(n-1)
    else :
        for i in range((n-2)//2) :
            print(i+2)
        print(1)
        print(n)
        for i in range((n-2)//2,0,-1) :
            print(n-i)

sol()