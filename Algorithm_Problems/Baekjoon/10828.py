if __name__ == '__main__':
    import sys
    from collections import deque
    input = sys.stdin.readline

    n=int(input())
    board = list(list(input().split()) for _ in range(n))
    res = deque()
    for command in board :
        if command[0] == "push" :
            res.append(command[1])
        if command[0] == "pop" :
            if res :
                print(res.pop())
            else :
                print(-1)
        if command[0] == "size" :
            print(len(res))
        if command[0] == "empty" :
            if res:
                print(0)
            else:
                print(1)
        if command[0] == "top" :
            if res :
                print(res[-1])
            else :
                print(-1)