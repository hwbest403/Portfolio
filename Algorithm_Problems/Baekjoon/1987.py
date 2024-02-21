# coding = utf-8

import sys
input = sys.stdin.readline

r, c = map(int,input().split())
board = list(input().rstrip() for _ in range(r))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def dfs(board, sx, sy) :
    res = 1
    need_visited = list()
    need_visited.append((sx, sy, board[sx][sy]))
    while need_visited :
        node = need_visited.pop()
        print(f"- 현재 노드, 경로 : {node}")
        print(need_visited)
        flag = 0
        for i in range(4) :
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny] not in node[2]:
                need_visited.append((nx, ny, node[2] + board[nx][ny]))
                print(f"  가야할 경로 : {(nx, ny, node[2] + board[nx][ny])}")
                res = max(res, len(node[2])+1)
                flag = 1
        if flag == 0 :
            print("  더 갈 수 있는 경로 없음(백트래킹)")
            print(f"  저장된 경로 : {need_visited}")
        print(f"  최대 depth : {res}")
    return res

print(dfs(board,0,0))