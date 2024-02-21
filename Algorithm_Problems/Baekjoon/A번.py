import sys
from itertools import combinations
input = sys.stdin.readline

n, x, y = map(int,input().split())
score = list(map(int,input().split()))

MOD = 998244353

flag = 0
resrat, res = 0, 0
for choice in combinations(score, 2) :
    if flag < n-1 :
        if choice[0] < choice[1] :
            resrat += y + y*((choice[1]-choice[0])//x)
            res += y + y*((choice[1]-choice[0])//x)
        elif choice[0] == choice[1] :
            pass
        else :
            res += y + y*((choice[0]-choice[1])//x)
        flag += 1
    else :
        if choice[0] < choice[1] :
            res += y + y*((choice[1]-choice[0])//x)
        elif choice[0] == choice[1] :
            pass
        else :
            res += y + y*((choice[0]-choice[1])//x)
print(res%MOD, resrat%MOD)