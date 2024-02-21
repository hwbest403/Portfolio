# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(list(input().split()) for _ in range(n))
        return n, board

    n, board = getdata()
