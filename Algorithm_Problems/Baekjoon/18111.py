# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n, m, b= map(int,input().split())
        return n, m, b

    n, m, b = getdata()
    board = list(0 for _ in range(n))
    minh, maxh = 257, -1
    for i in range(n) :
        board[i]=list(map(int,input().split()))
        for j in range(m) :
            if board[i][j]<=minh :
                minh = board[i][j]
            if board[i][j]>=maxh :
                maxh = board[i][j]

    minsec, res = 10**9, 0
    for case in range(minh, maxh+1) :
        sec, tmp = 0, b
        for i in range(n) :
            for j in range(m) :
                if board[i][j] > case :
                    sec += (board[i][j]-case) * 2
                    tmp += board[i][j]-case
                else :
                    sec += case - board[i][j]
                    tmp -= case - board[i][j]
        if tmp >= 0 :
            if sec < minsec :
                minsec = sec
                res = case
    print(minsec, res)