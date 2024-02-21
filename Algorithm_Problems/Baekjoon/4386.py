# coding = utf-8

if __name__ == '__main__':
    import sys
    import math as m
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(list(map(float, input().split())) for _ in range(n))
        return n, board

    n, board = getdata()
    edge = list()
    for i in range(n-1) :
        for j in range(i+1, n) :
            weight = round(m.sqrt((board[i][0]-board[j][0])**2+(board[i][1]-board[j][1])**2),2)
            edge.append([i, j, weight])
    edge.sort(key=lambda x:x[2], reverse=False)
    par = list(i for i in range(n))
    def find(a) :
        if a==par[a] :
            return a
        else :
            par[a] = find(par[a])
            return par[a]
    def union(a,b) :
        a, b = find(a), find(b)
        if a<b :
            par[b] = a
        else :
            par[a] = b
    total_weight = 0
    for e in edge :
        lv, rv, w = e[0], e[1], e[2]
        if find(lv) != find(rv) :
            total_weight += w
            union(lv, rv)
    print(total_weight)