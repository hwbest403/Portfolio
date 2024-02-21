# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    from collections import deque
    from itertools import *

    def getdata():
        n = int(input())
        m = int(input())
        board = list(list(map(int, input().split())) for _ in range(m))
        return n, m, board

    n, m, board = getdata()
    gp = dict()
    for i in range(1,n+1) :
        gp[i] = list()
    for e in board :
        gp[e[0]].append(e[1])
        gp[e[1]].append(e[0])
    print(gp)

    def dfs(gp, s) :
        need_visited, visited = deque(), deque()
        need_visited.append(s)
        print(need_visited)
        while need_visited :
            node = need_visited.pop()
            if node not in visited :
                print(node)
                visited.append(node)
                need_visited.extend(gp[node])
                print(need_visited)
        print(visited)
        return len(visited)

    print(dfs(gp,1)-1)