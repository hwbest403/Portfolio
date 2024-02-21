# coding = utf-8
import sys
input = sys.stdin.readline

bn = 5
bingo = list(list(map(int,input().split())) for _ in range(bn))
call = list(list(map(int,input().split())) for _ in range(bn))
visited = list(list(False for _ in range(bn)) for _ in range(bn))

def printboard(board) :
    for row in board :
        print(row)


def erasenum(n, bingo, visited) :
    for i in range(bn) :
        for j in range(bn) :
            if bingo[i][j] == n :
                visited[i][j] = True
                return

def checkbingo(visited) :
    ch = 0
    # 가로 check
    for row in visited :
        if row.count(True) == bn :
            ch += 1
    # 세로 check
    for i in range(bn) :
        tmp = 0
        for j in range(bn) :
            if visited[j][i] == True :
                tmp += 1
        if tmp == bn :
            ch += 1
    # 좌상 우하 대각선 check
    tmp = 0
    for i in range(bn) :
        if visited[i][i] == True :
            tmp += 1
    if tmp == bn :
        ch += 1
    # 우상 좌하 대각선 check
    tmp = 0
    for i in range(bn):
        if visited[i][-i-1] == True:
            tmp += 1
    if tmp == bn:
        ch += 1

    return ch

def sol() :
    res = 0
    for row in call :
        for num in row :
            erasenum(num, bingo, visited)
            res += 1
            if checkbingo(visited) >= 3 :
                return res

print(sol())