# coding = utf-8

import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

edge = defaultdict(list)
reverse_edge = defaultdict(list)
v,e = map(int,input().split())
for _ in range(e) :
    lv, rv = map(int,input().split())
    edge[lv].append(rv)
    reverse_edge[rv].append(lv)

visited = list(False for _ in range(v+1))
r_visited = list(False for _ in range(v+1))
stack = list()
def dfs(node) :
    visited[node] = True
    for next_node in edge[node] :
        if not visited[next_node] :
            dfs(next_node)
    stack.append(node)
def reverse_dfs(node,tmp) :
    r_visited[node] = True
    tmp.append(node)
    for next_node in reverse_edge[node] :
        if not r_visited[next_node] :
            reverse_dfs(next_node,tmp)
for i in range(1,v+1) :
    if not visited[i] :
        dfs(i)
res = list()
while stack :
    tmp = list()
    node = stack.pop()
    if not r_visited[node] :
        reverse_dfs(node,tmp)
        res.append(sorted(tmp))
res = sorted(res)
print(len(res))
for i in res :
    print(*i, end=" -1\n")
