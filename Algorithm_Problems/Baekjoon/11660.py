# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def sumboard(board, n) :
        res = list(0 for _ in range(n+1))
        res[0]=0
        for i in range(1, n+1) :
            res[i]=res[i-1]+board[i-1]
        return res

    def prefix(board, a, b) :
        return board[b] - board[a-1]

    def getdata():
        n, m = map(int,input().split())
        board = list()
        for _ in range(n) :
            tmp = list(map(int,input().split()))
            board.append(sumboard(tmp,n))
        case = list(list(map(int,input().split())) for _ in range(m))
        return n, m, board, case

    n, m, board, case = getdata()
    for c in case :
        res = 0
        for i in range(c[0]-1,c[2]) :
            res+=prefix(board[i], c[1], c[3])
        print(res)