# coding = utf-8

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def bubblesort(A, B, n) :
    if A == B :
        print(1)
        return

    for last in range(n,1,-1) :
        for i in range(last-1) :
            if A[i] > A[i+1] :
                tmp = A[i+1]
                A[i+1] = A[i]
                A[i] = tmp
                if A[i+1] == B[i+1] :
                    if A == B :
                        print(1)
                        return

    print(0)
    return

bubblesort(A, B, n)