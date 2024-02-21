# coding = utf-8

import sys
input = sys.stdin.readline

board = list(list(map(int,list(input().rstrip()))) for _ in range(9))
zero = list()
for i in range(9) :
    for j in range(9) :
        if board[i][j] == 0 :
            zero.append([i,j])

def printboard(board) :
    for row in board :
        for num in row :
            print(num, end="")
        print()

def sol(n) :
    if len(zero) == n :
        printboard(board)
        sys.exit()

    x, y = zero[n]
    num_list = list(i for i in range(1, 10))

    for i in range((x//3)*3, (x//3+1)*3) :
        for j in range((y//3)*3, (y//3+1)*3) :
            if board[i][j] in num_list :
                num_list.remove(board[i][j])

    for i in range(9) :
        if board[x][i] in num_list :
            num_list.remove(board[x][i])
        if board[i][y] in num_list :
            num_list.remove(board[i][y])

    for i in num_list :
        board[x][y] = i
        sol(n+1)
    board[x][y] = 0

sol(0)