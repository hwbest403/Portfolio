# coding = utf-8

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
cloud = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]
dx = [0,0,-1,-1,-1,0,1,0,1]
dy = [0,-1,-1,0,1,1,1,1,-1]

def move(cloud:list, d:int, s:int):
    # 1
    for i in range(len(cloud)):
        cloud[i][0], cloud[i][1] = (cloud[i][0]+s*dx[d])%n, (cloud[i][1]+s*dy[d])%n

def rain(cloud:list, board:list):
    # 2
    for c in cloud:
        board[c[0]][c[1]] += 1
        for i in range(2, 9, 2):
            nx, ny = c[0]+dx[i], c[1]+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] != 0:
                    board[c[0]][c[1]] += 1

def makecloud(visited:list)->list:
    new_cloud = list()
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and [i, j] not in visited:
                new_cloud.append([i, j])
                board[i][j] -= 2
    return new_cloud

def sol(cloud:list, d:int, s:int):
    move(cloud, d, s)
    rain(cloud, board)
    new_cloud = makecloud(cloud)
    return new_cloud

def printboard(board):
    for row in board:
        print(row)

printboard(board)
for i in range(m):
    print(f"=={i+1}th")
    d, s = map(int, input().split())
    cloud = sol(cloud, d, s)
    printboard(board)
