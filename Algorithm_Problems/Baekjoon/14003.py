# coding = utf-8

if __name__ == '__main__':
    import sys
    from collections import deque
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(map(int, input().split()))
        return n, board

    # while문 logN 시간복잡도
    def bs(lis, a) :
        s, e = 0, len(lis) - 1
        while s<e :
            mp = (s+e) // 2
            if lis[mp] >= a :
                e = mp
            else :
                s = mp+1
        return s

    # for문 N 시간복잡도
    def sol(board, n) :
        lis = list()
        rec = list()
        lis.append(2 * (10 ** 6))
        for i in range(n):
            if lis[-1] < board[i]:
                rec.append([len(lis),board[i]])
                lis.append(board[i])
            else:
                idx = bs(lis, board[i])
                lis[idx] = board[i]
                rec.append([idx, board[i]])
        return lis, rec

    # sol->bs = NlogN 시간복잡도
    n, board = getdata()
    lis, rec = sol(board, n)
    res = deque()
    ans = len(lis)
    print(ans)
    for i in range(n-1,-1,-1) :
        if rec[i][0] == ans-1 :
            res.appendleft(rec[i][1])
            ans -= 1
            if ans == -1 :
                break
    print(*res)