import sys
import copy
input = sys.stdin.readline

n, k = list(map(int,input().split()))
board = list(map(int, input().split()))

def printbelt(board) :
    for i in range(n):
        print(board[i], end=' ')
    print()
    for i in range(2*n-1, n-1, -1) :
        print(board[i], end=' ')
    print()
    return

print("start")
printbelt(board)

def beltmove(board) :
    tmp = board[2*n-1]
    for i in range(2*n-1, 0, -1) :
        board[i] = board[i-1]
    board[0] = tmp
    return

def sol(board) :
    copy_board = copy.deepcopy(board)
    visited = list(0 for _ in range(2*n))
    ind = 1
    while True :
        print(f"==={ind}")
        # 1th rule
        beltmove(copy_board)
        beltmove(visited)
        if visited[n-1] == 1:
            visited[n-1] = 0
        if copy_board.count(0) >= k :
            return ind
            break
        # 2nd rule
        for i in range(n-2, -1, -1) :
            if visited[i] == 1 and visited[i+1] == 0 and copy_board[i+1] != 0:
                visited[i] = 0
                visited[i+1] = 1
                copy_board[i+1] -= 1
        if visited[n-1] == 1 :
            visited[n-1] = 0
        if copy_board.count(0) >= k:
            return ind
            break
        # 3rd rule0
        if copy_board[0] != 0 :
            visited[0] = 1
            copy_board[0] -= 1
        if copy_board.count(0) >= k:
            return ind
            break
        ind += 1
        printbelt(copy_board)
        print("-")
        printbelt(visited)

print(sol(board))
