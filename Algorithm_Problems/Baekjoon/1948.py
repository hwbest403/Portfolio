# coding = utf-8
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input())
m = int(input())
indeg = list(0 for _ in range(n+1))
indeg[0] = -1
gp = defaultdict(list)
for _ in range(m):
    lv, rv, w = map(int, input().split())
    gp[lv].append([rv, w])
    indeg[rv] += 1
start, end = map(int, input().split())
q = deque()
q.append(start)
weight = list(0 for _ in range(n+1))
count = list(list() for _ in range(n+1))
while q :
    node = q.popleft()
    for nx in gp[node] :
        indeg[nx[0]] -= 1
        if weight[nx[0]] < weight[node] + nx[1] :
            weight[nx[0]] = weight[node] + nx[1]
            count[nx[0]] = [node]
        elif weight[nx[0]] == weight[node] + nx[1] :
            count[nx[0]].append(node)
        if indeg[nx[0]] == 0 :
            q.append(nx[0])

q = deque([end])
path = set()
while q:
    node = q.popleft()
    for nx in count[node] :
        if (node, nx) not in path :
            path.add((node, nx))
            q.append(nx)
print(weight[end])
print(len(path))