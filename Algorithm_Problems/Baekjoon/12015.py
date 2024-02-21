# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(map(int, input().split()))
        return n, board

    def bs(lis, a) :
        s, e = 0, len(lis) - 1
        while s<e :
            mp = (s+e) // 2
            if lis[mp] >= a :
                e = mp
            else :
                s = mp+1
        return s

    def sol(board, n) :
        lis = list()
        lis.append(0)
        for i in range(n) :
            if lis[-1] < board[i] :
                lis.append(board[i])
            else :
                idx = bs(lis, board[i])
                lis[idx] = board[i]
        return lis

    n, board = getdata()
    lis = sol(board, n)
    print(len(lis)-1)