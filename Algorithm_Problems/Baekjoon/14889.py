from collections import deque
import copy
import sys
import itertools

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ls = []
print(arr)
for row in arr :
    print(row)

choice=list(itertools.combinations([0,1,2,3],2))
print(choice)

minval = 100

for i in range(int(len(choice)/2)) :
    tmp = list(itertools.permutations(choice[i],2))
    ver = list(itertools.permutations(choice[-i-1],2))
    tmpval, verval = 0, 0
    for j in range(len(tmp)) :
        tmpval += arr[tmp[j][0]][tmp[j][1]]
        verval += arr[ver[j][0]][ver[j][1]]
    if minval > abs(tmpval-verval) :
        minval = abs(tmpval-verval)

print(minval)