# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    board = str(input())
    if not board :
        print(0)
        sys.exit()
    board = board.lstrip().rstrip()
    board = list(board.split())
    print(len(board))