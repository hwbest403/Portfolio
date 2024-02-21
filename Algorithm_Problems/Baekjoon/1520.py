# coding = utf-8

if __name__ == '__main__':
    import sys
    from collections import deque
    input = sys.stdin.readline

    def getdata():
        n, m = map(int,input().split())
        board = list(list(map(int, input().split())) for _ in range(n))
        return n, m, board

    def printdp(dp) :
        for row in dp :
            print(row)

    n, m, board = getdata()
    gp = dict()
    for i in range(n) :
        for j in range(m) :
            gp[i,j] = list()
            if 0<=i-1 and board[i-1][j] < board[i][j] :
                gp[i,j].append([i-1,j])
            if 0<=j-1 and board[i][j-1] < board[i][j] :
                gp[i,j].append([i,j-1])
            if i+1<n and board[i+1][j] < board[i][j] :
                gp[i,j].append([i+1,j])
            if j+1<m and board[i][j+1] < board[i][j] :
                gp[i,j].append([i,j+1])
    print(gp)
    def dfs(gp, s, e) :
        res = 0
        need_visited, visited = deque(), deque()
        dis = dict()
        need_visited.append(s)
        dis[s[0],s[1]] = 1
        while need_visited :
            node = need_visited.popleft()
            if node not in visited :
                visited.append(node)
                di = 0
                for ele in gp[node[0],node[1]] :
                    dis[ele[0],ele[1]] = dis[node[0],node[1]] + di
                    di += 1
        return res
    print(dfs(gp,[0,0],[n-1,m-1]))