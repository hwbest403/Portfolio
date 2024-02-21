# coding = utf-8

import sys
input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()

def getpi(P) :
    pi = list(0 for _ in range(len(P)))
    j = 0
    for i in range(1, len(P)) :
        while P[j] != P[i] and j>0 :
            j = pi[j-1]
        if P[j] == P[i] :
            j += 1
            pi[i] = j
    return pi

pi = getpi(P)
res = list()
j = 0
for i in range(len(T)) :
    while j>0 and T[i] != P[j] :
        j = pi[j-1]
    if T[i] == P[j] :
        if j == len(P) - 1 :
            res.append(i-len(P)+2)
            j = pi[j]
        else :
            j += 1
print(len(res))
print(*res)