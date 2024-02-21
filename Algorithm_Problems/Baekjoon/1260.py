# coding = utf-8

if __name__ == '__main__':
    import sys
    from collections import deque
    import copy
    input = sys.stdin.readline

    def getdata():
        n, m, s = map(int,input().split())
        board = list(list(map(int, input().split())) for _ in range(m))
        return n, m, s, board

    n, m, s, board = getdata()
    gpb = dict()
    for i in range(1,n+1) :
        gpb[i] = list()
    for e in board :
        gpb[e[0]].append(e[1])
        gpb[e[1]].append(e[0])
    gpd = copy.deepcopy(gpb)
    for i in range(1, n+1) :
        gpb[i].sort(reverse=False)
        gpd[i].sort(reverse=True)
    print(gpb)
    print(gpd)

    def bfs(gp, start) :
        visited, need_visited = deque(), deque()
        need_visited.append(start)
        while need_visited :
            next_node = need_visited.popleft()
            if next_node not in visited :
                visited.append(next_node)
                need_visited.extend(gp[next_node])
        return visited

    def dfs(gp, start) :
        visited, need_visited = deque(), deque()
        need_visited.append(start)
        while need_visited :
            next_node = need_visited.pop()
            if next_node not in visited :
                visited.append(next_node)
                need_visited.extend(gp[next_node])
        return visited


    d_visited = dfs(gpd, s)
    b_visited = bfs(gpb, s)
    print(*d_visited)
    print(*b_visited)