# coding = utf-8

if __name__ == '__main__':
    import sys
    from collections import deque
    input = sys.stdin.readline

    def printboard(board) :
        for row in board :
            print(row)

    def getdata():
        n, m = map(int,input().split())
        sx, sy = map(int,input().split())
        ex, ey = map(int,input().split())
        board = list(list(map(int, input().split())) for _ in range(n))
        return n, m, sx-1, sy-1, ex-1, ey-1, board

    n, m, sx, sy, ex, ey, board = getdata()

    def bfs(board, sx, sy, ex, ey) :
        visited, need_visited = deque(), deque()
        distance = dict()
        start = [sx, sy]
        distance[sx, sy] = 0
        need_visited.append(start)
        while need_visited :
            tmp = need_visited.popleft()
            tx, ty = tmp[0], tmp[1]
            visited.append(tmp)
            next = list()
            if 0 <= tx - 1 and board[tx - 1][ty] == 0 and [tx-1, ty] not in visited :
                next.append([tx-1, ty])
            if 0 <= ty - 1 and board[tx][ty-1] == 0 and [tx, ty-1] not in visited:
                next.append([tx, ty-1])
            if tx + 1 < n and board[tx + 1][ty] == 0 and [tx+1, ty] not in visited:
                next.append([tx + 1, ty])
            if ty + 1 < m and board[tx][ty+1] == 0 and [tx, ty+1] not in visited:
                next.append([tx, ty+1])
            need_visited.extend(next)
            for node in next :
                distance[node[0],node[1]] = distance[tx,ty] + 1
                if node[0] == ex and node[1] == ey :
                    return distance[ex, ey]
        return 10**6

    def sol(board, wall, res) :
        if wall == 1 :
            ans = bfs(board, sx, sy, ex, ey)
            if ans < res :
                res = ans
            return res
        for i in range(n) :
            for j in range(m) :
                if board[i][j] == 1 :
                    board[i][j] = 0
                    res = sol(board, 1, res)
                    board[i][j] = 1
        if res == 10**6 :
            return -1
        else :
            return res
    print(sol(board, 0, 10**6))