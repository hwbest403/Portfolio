import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int,input().split())
edge = defaultdict(list)
deg = list(0 for _ in range(n+1))
res = deque()
for _ in range(m) :
    a, b = map(int,input().split())
    edge[a].append(b)
    deg[b] += 1

for i in range(1, n+1) :
    if deg[i] == 0 :
        res.append(i)

ans = list()
while res :
    now = res.popleft()
    ans.append(now)
    for i in edge[now] :
        deg[i] -= 1
        if deg[i] == 0 :
            res.append(i)

print(*ans)