# coding = utf-8

import sys
input = sys.stdin.readline

r, c = map(int,input().split())
board = list(input().rstrip() for _ in range(r))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def dfs(board, sx, sy) :
    res = 1
    need_visited = set()
    need_visited.add((sx, sy, board[sx][sy]))
    while need_visited :
        node = need_visited.pop()
        for i in range(4) :
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny] not in node[2]:
                need_visited.add((nx, ny, node[2] + board[nx][ny]))
                res = max(res, len(node[2])+1)
    return res

print(dfs(board,0,0))