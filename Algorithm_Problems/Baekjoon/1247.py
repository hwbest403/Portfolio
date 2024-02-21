# coding = utf-8

import sys
input = sys.stdin.readline

for _ in range(3) :
    n = int(input())
    board = list()
    for _ in range(n) :
        board.append(int(input()))
    if sum(board) > 0 :
        print("+")
    elif sum(board) == 0 :
        print("0")
    else :
        print("-")