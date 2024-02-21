# coding = utf-8
import copy
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
chess = list(list(list() for _ in range(n)) for _ in range(n))
loc = list(list() for _ in range(k))
di = list(0 for _ in range(k))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(k) :
    r, c, d = map(int, input().split())
    loc[i] = [r-1, c-1]
    di[i] = d-1
    chess[r-1][c-1].append(i)

def printboard(board):
    for row in board:
        print(row)

def move(l, direc):
    return l[0]+dx[direc], l[1]+dy[direc]

def turndirection(direc):
    if direc == 0:
        return 1
    elif direc == 1:
        return 0
    elif direc == 2:
        return 3
    else:
        return 2

def blue(idx):
    tx, ty = copy.deepcopy(loc[idx][0]), copy.deepcopy(loc[idx][1])
    di[idx] = turndirection(di[idx])
    nx, ny = move(loc[idx], di[idx])
    if nx<0 or nx>=n or ny<0 or ny>=n:
        nx, ny = tx, ty
    elif board[nx][ny] == 2:
        nx, ny = tx, ty
    flag = False
    for k in copy.deepcopy(chess[tx][ty]):
        if idx == k:
            flag = True
        if not flag:
            continue
        chess[tx][ty].remove(k)
        chess[nx][ny].append(k)
        loc[k] = [nx, ny]

def red(idx, i, j):
    tx, ty = copy.deepcopy(loc[idx][0]), copy.deepcopy(loc[idx][1])
    flag = True
    for k in copy.deepcopy(chess[tx][ty][::-1]):
        if not flag:
            continue
        if idx == k:
            flag = False
        chess[tx][ty].remove(k)
        chess[i][j].append(k)
        loc[k] = [i, j]

def white(idx, i, j):
    tx, ty = copy.deepcopy(loc[idx][0]), copy.deepcopy(loc[idx][1])
    flag = False
    for k in copy.deepcopy(chess[tx][ty]):
        if idx == k:
            flag = True
        if not flag:
            continue
        chess[tx][ty].remove(k)
        chess[i][j].append(k)
        loc[k] = [i,j]

def turn():
    for i in range(k):
        nx, ny = move(loc[i], di[i])
        if nx<0 or ny<0 or nx>=n or ny>=n:
            blue(i)
        elif board[nx][ny] == 2:
            blue(i)
        elif board[nx][ny] == 1:
            red(i, nx, ny)
        else :
            white(i, nx, ny)

def checkchess():
    for i in range(n):
        for j in range(n):
            if len(chess[i][j]) >= 4:
                return True
    return False

printboard(chess)
for i in range(1001):
    print(f"==={i+1}th")
    turn()
    printboard(chess)
    if checkchess():
        print(i+1)
        sys.exit()
print(-1)