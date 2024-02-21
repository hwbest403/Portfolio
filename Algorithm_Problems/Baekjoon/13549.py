import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
visited = list(-1 for _ in range(100001))
visited[n] = 0

def bfs(n, k):
    need_visited = deque()
    need_visited.append(n)
    while need_visited:
        x = need_visited.popleft()
        if x == k:
            return visited[x]
        if 0<= x*2 < 100001 and visited[x*2] == -1:
            visited[x*2] = visited[x]
            need_visited.append(x*2)
        if 0<= x-1 < 100001 and visited[x-1] == -1:
            visited[x-1] = visited[x] + 1
            need_visited.append(x-1)
        if 0<= x+1 < 100001 and visited[x+1] == -1:
            visited[x+1] = visited[x] + 1
            need_visited.append(x+1)

print(bfs(n,k))