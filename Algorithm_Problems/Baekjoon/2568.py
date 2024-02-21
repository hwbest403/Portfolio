# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque

    def getdata():
        n = int(input())
        board = list(list(map(int, input().split())) for _ in range(n))
        return n, board

    def bs(lis, a) :
        s, e = 0, len(lis) - 1
        while s<e :
            mp = (s+e) // 2
            if lis[mp][1] >= a :
                e = mp
            else :
                s = mp+1
        return s

    def sol(board, n) :
        lis = deque()
        rec = deque(-1 for _ in range(n))
        lis.append([0,500001])
        for i in range(n) :
            if lis[-1][1] < board[i][1] :
                rec[i] = len(lis)
                lis.append(board[i])
            else :
                idx = bs(lis, board[i][1])
                lis[idx] = board[i]
                rec[i] = idx
        return lis, rec

    n, board = getdata()
    board.sort(key=lambda x:x[0],reverse=False)
    lis, rec = sol(board, n)
    res = len(lis)
    print(n-res)
    tmp = deque()
    for i in range(n-1,-1,-1) :
        if rec[i] == res - 1 :
            res -= 1
        else :
            tmp.appendleft(i)
    for i in tmp :
        print(board[i][0])