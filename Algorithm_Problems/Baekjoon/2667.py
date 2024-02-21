if __name__ == '__main__' :
    import sys
    input = sys.stdin.readline
    from collections import deque

    n = int(input())
    board = list(list(input()) for _ in range(n))
    graph = dict()

    for i in range(n) :
        board[i].pop()
        for j in range(n) :
            tmp = list()
            if board[i][j] == '1' :
                if i-1 >= 0 and board[i-1][j] == '1' :
                    tmp.append((i-1)*n+j)
                if j-1 >= 0 and board[i][j-1] == '1' :
                    tmp.append(i*n+j-1)
                if i+1 < n and board[i+1][j] == '1' :
                    tmp.append((i+1)*n+j)
                if j+1 < n and board[i][j+1] == '1' :
                    tmp.append(i*n+j+1)
                graph[i*n+j] = tmp

    def bfs() :
        need, visited = deque(), deque()
        total = 0
        house = list()
        for i in range(n) :
            for j in range(n) :
                if i*n+j in graph.keys() :
                    if i*n+j not in visited :
                        tmp = list()
                        need.append(i*n+j)
                        while need :
                            next = need.pop()
                            if next not in visited :
                                visited.append(next)
                                tmp.append(next)
                                need.extend(graph[next])
                        house.append(tmp)
                        total += 1

        print(total)
        for i in range(total) :
            house[i] = len(house[i])
        house.sort(reverse=False)
        for i in range(total) :
            print(house[i])
    bfs()