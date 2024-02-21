# coding = utf-8

import sys
input = sys.stdin.readline

n = int(input())
visited = list(list(False for _ in range(101)) for _ in range(101))
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def rotate(x, y, ox, oy) :
    return -(y-oy)+ox, x-ox+oy

def curve(x, y, d, g) :
    dot = set()
    dot.add((x, y))
    visited[x][y] = True
    ox, oy = x + dx[d], y + dy[d]
    dot.add((ox, oy))
    visited[ox][oy] = True
    for i in range(g) :
        tmp = list()
        for j in range(len(list(dot))) :
            if (ox, oy) == list(dot)[j] :
                continue
            nx, ny = rotate(list(dot)[j][0], list(dot)[j][1], ox, oy)
            tmp.append((nx, ny))
            visited[nx][ny] = True
        ox, oy = rotate(x, y, ox, oy)
        for t in tmp :
            dot.add(t)

for _ in range(n) :
    x, y, d, g = map(int,input().split())
    curve(x, y, d, g)

res = 0
for i in range(100) :
    for j in range(100) :
        if visited[i][j] and visited[i][j+1] and visited[i+1][j] and visited[i+1][j+1] :
            res += 1
print(res)