if __name__ == '__main__' :
    import sys
    input = sys.stdin.readline
    from collections import deque

    board = list(list(input()) for _ in range(10))
    print(board)
    for i in range(10) :
        board[i].pop()
    