# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque

    def getdata():
        n, m = map(int,input().split())
        board = list(list(map(int, input().split())) for _ in range(m))
        return n,m,board

    n,m,board = getdata()
    par = list(i for i in range(n))

    def find(a) :
        if a == par[a] :
            return a
        else :
            par[a] = find(par[a])
            return par[a]

    def union(a, b) :
        a, b = find(a), find(b)
        if a>b :
            par[a] = b
        else :
            par[b] = a
        return

    cnt = 0
    for i in range(m) :
        lv, rv = board[i][0], board[i][1]
        # 같은 트리 X -> cycle X
        if find(lv) != find(rv) :
            union(lv, rv)
            cnt += 1
        else :
            print(i+1)
            break
    if cnt == m :
        print(0)