if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    while True :
        board = list(map(int,input().split()))
        if board[0] == 0 :
            break
        idx = board.index(max(board))
        if board[idx] ** 2 == board[(idx+1)%3] ** 2 + board[(idx+2)%3] ** 2 :
            print('right')
        else :
            print('wrong')