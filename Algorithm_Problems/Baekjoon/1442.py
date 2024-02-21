# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        k, n = map(int,input().split())
        board = list()
        for i in range(k) :
            board.append(int(input()))
        return k, n, board

    k, n, board = getdata()
    for i in range(n-k) :
        board.append(max(board))
