# coding = utf-8

import sys
input = sys.stdin.readline
from collections import  deque

T = int(input())
for idx in range(T) :
    h, w = map(int,input().split())
    board = list(list(input().rstrip()) for _ in range(h))
    key = list(input().rstrip())
    key_visited = list(False for _ in range(26))
    for k in key :
        if k == '0' :
            break
        key_visited[ord(k)-97] = True
    visited = list(list(False for _ in range(w)) for _ in range(h))
    door = list()
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    def findstart() :
        startpoint = list()
        res = 0
        for i in range(h) :
            for j in range(w) :
                if i == 0 or i == h-1 or j == 0 or j == w-1 :
                    if 65<=ord(board[i][j])<=90 :
                        if key_visited[ord(board[i][j])-65] :
                            board[i][j] = '.'
                        else :
                            door.append([board[i][j],i,j])
                    if 97 <= ord(board[i][j]) <= 122:
                        key_visited[ord(board[i][j]) - 97] = True
                        board[i][j] = '.'
                    if board[i][j] == '$' :
                        res += 1
                        board[i][j] = '.'
                    if board[i][j] == '.' :
                        startpoint.append([i, j])
        return startpoint, res

    def dfs(start) :
        res = 0
        need_visited = deque()
        for s in start :
            need_visited.append(s)
        while need_visited :
            now = need_visited.popleft()
            if visited[now[0]][now[1]] == False :
                visited[now[0]][now[1]] = True
                for i in range(4) :
                    nx, ny = now[0]+dx[i], now[1]+dy[i]
                    if nx >= h or nx < 0 or ny < 0 or ny >= w  :
                        continue
                    if board[nx][ny] == '*' :
                        continue
                    if 97<=ord(board[nx][ny])<=122 :
                        key_visited[ord(board[nx][ny])-97] = True
                        board[nx][ny] = '.'
                        need_visited.append([nx, ny])
                        continue
                    if 65<=ord(board[nx][ny])<=90 :
                        door.append([board[nx][ny],nx,ny])
                        continue
                    if ord(board[nx][ny]) == 36 :
                        res += 1
                        board[nx][ny] = '.'
                        need_visited.append([nx, ny])
                        continue
                    need_visited.append([nx, ny])
            if len(need_visited) == 0 :
                for idx, d in enumerate(door) :
                    if key_visited[ord(d[0])-65] :
                        need_visited.append([d[1], d[2]])
                        del door[idx]
                        break
        return res

    startpoint, ans = findstart()
    ans += dfs(startpoint)
    print(ans)