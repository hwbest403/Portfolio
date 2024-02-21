# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from functools import cmp_to_key

    def getdata():
        k, n = map(int,input().split())
        board = list()
        for _ in range(k) :
            tmp = int(input())
            board.append(tmp)
        return k, n, board

    k, n, board = getdata()
    board.sort(reverse=False)
    for _ in range(n-k) :
        board.append(board[-1])
    board.sort(key=cmp_to_key(lambda x,y : int(str(y)+str(x))-int(str(x)+str(y))))
    for i in board :
        print(i,end="")