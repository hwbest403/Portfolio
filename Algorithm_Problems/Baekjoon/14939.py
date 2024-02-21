# coding = utf-8

if __name__ == '__main__':
    import sys
    import copy
    from itertools import combinations
    input = sys.stdin.readline

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def getdata():
        board = list()
        for i in range(10) :
            board.append(list(input()))
            board[i].pop()
        return board

    def printboard(board) :
        for i in range(10) :
            print(board[i])

    def switch(board, x, y) :
        if board[x][y] == '#' :
            board[x][y] = 'O'
        else :
            board[x][y] = '#'
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<10 and 0<=ny<10 :
                if board[nx][ny] == '#' :
                    board[nx][ny] = 'O'
                else :
                    board[nx][ny] = '#'
        return board

    def sol(board) :
        minval = 1000
        for i in range(1, 11) :
            for choice in combinations([k for k in range(10)], i) :
                copy_board = copy.deepcopy(board)
                cnt, flag = 0, 0
                for j in choice :
                    copy_board = switch(copy_board, 0, j)
                    cnt += 1
                for l in range(1,10) :
                    for m in range(10) :
                        if copy_board[l-1][m] == 'O' :
                            copy_board = switch(copy_board, l, m)
                            cnt += 1
                for n in range(10) :
                    if copy_board[9][n] == "O" :
                        flag = 1
                        break
                if flag == 0 :
                    if cnt < minval :
                        minval = cnt
                    # print(choice)
                    # print(flag, cnt, minval)
                    # printboard(copy_board)

        copy_board = copy.deepcopy(board)
        cnt, flag = 0, 0
        for i in range(1,10) :
            for j in range(10) :
                if copy_board[i-1][j] == "O" :
                    copy_board=switch(copy_board,i,j)
                    cnt+=1
                    # print(f"==={i}th_{j}th===")
                    # printboard(copy_board)
        for i in range(10) :
            if copy_board[9][i] == "O" :
                flag = 1
                break
        if flag == 0 :
            if cnt<minval :
                minval = cnt
        # print("last===")
        # print(flag, cnt, minval)
        # printboard(copy_board)
        if minval == 1000 :
            return -1
        return minval

    board=getdata()
    print(sol(board))