# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n, k = map(int,input().split())
        board = list(list(map(int, input().split())) for _ in range(n))
        mal = list()
        for _ in range(k) :
            tmp = list(map(int,input().split()))
            tmp[0] -= 1
            tmp[1] -= 1
            mal.append(tmp)
        return n, k, board, mal

    def printboard(board):
        for row in board :
            print(row)

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def move(x, y, dir) :
        nx = x+dx[dir]
        ny = y+dy[dir]

    n, k, board, mal = getdata()
