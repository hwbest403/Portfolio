import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
tree = defaultdict(list)
for _ in range(n-1) :
    lv, rv = map(int,input().split())
    tree[lv].append(rv)
    tree[rv].append(lv)
print(tree)
m = int(input())
for _ in range(m) :
    lv, rv = map(int,input().split())