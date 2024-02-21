# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        r, c = map(int,input().split())
        board = list(list(input().rstrip()) for _ in range(r))
        n = int(input())
        command=list()
        for _ in range(n) :
            tmp = int(input())
            command.append(tmp)
        return r, c, board, n, command

    r, c, board, n, command = getdata()

    def printboard(board) :
        for row in board :
            for i in row :
                print(i, end="")
            print()

    for i in command :
        tx, ty = 0, i-1
        while True :
            if tx+1>=r :
                board[tx][ty] = 'O'
                break
            if board[tx+1][ty] == 'X' :
                board[tx][ty] = 'O'
                break
            if board[tx+1][ty] == 'O' :
                if ty-1>=0 and board[tx][ty-1] == '.' and board[tx+1][ty-1] == '.' :
                    ty -= 1
                elif ty+1<c and board[tx][ty+1] == '.' and board[tx+1][ty+1] == '.' :
                    ty += 1
                else :
                    board[tx][ty] = 'O'
                    break
            tx += 1
    printboard(board)