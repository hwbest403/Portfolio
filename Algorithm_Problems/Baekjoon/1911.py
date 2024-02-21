# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n, l = map(int,input().split())
        board = list(list(map(int, input().split())) for _ in range(n))
        return n, l, board

    n, l, board = getdata()
    ls = list()
    for row in board :
        for i in range(row[0],row[1]) :
            ls.append(i)
    ls.sort(reverse=False)
    ls2 = list()
    res = 0
    for i in ls :
        if i not in ls2 :
            res += 1
            ls2.extend([i,i+1,i+2])
    # print(ls)
    # print(ls2)
    print(res)