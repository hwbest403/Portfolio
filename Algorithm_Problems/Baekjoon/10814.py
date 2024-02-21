# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(list(input().split()) for _ in range(n))
        return n, board

    n, board = getdata()
    for i in range(n) :
        board[i][0] = int(board[i][0])
    board.sort(key=lambda x:x[0],reverse=False)
    for x in board :
        print(x[0], x[1])
