# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n, m, k = map(int,input().split())
        board = list(list(map(int, input().split())) for _ in range(n))
        w = int(input())
        wall = list(list(map(int,input().split())) for _ in range(w))
        return n, m, k, board, w, wall

    n,m,k,board,w,wall = getdata()
