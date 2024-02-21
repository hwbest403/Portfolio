# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque

    def getdata():
        n = int(input())
        board = list(list(input().split()) for _ in range(n))
        return n, board

    n,board = getdata()
    res = deque()
    for case in board :
        if case[0] == "push" :
            res.append(case[1])
        elif case[0] == "front" :
            if res :
                print(res[0])
                continue
            print(-1)
        elif case[0] == "back" :
            if res:
                print(res[-1])
                continue
            print(-1)
        elif case[0] == "size" :
            print(len(res))
        elif case[0] == "empty" :
            if res :
                print(0)
                continue
            print(1)
        elif case[0] == "pop" :
            if res:
                print(res.popleft())
                continue
            print(-1)