if __name__ == '__main__':
    import sys
    import copy
    input = sys.stdin.readline

    n, m = map(int,input().split())
    board = list(list(map(int,input().rstrip())) for _ in range(n))
    dx=[0,0,1,-1]
    dy=[-1,1,0,0]

    def dfs(board, x, y, visited) :
        visited.append([x,y])
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0 and [nx, ny] not in visited:
                dfs(board, nx, ny, visited)

    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 1 :
                visited=[]
                dfs(board, i, j, visited)
                print(len(visited),end="")
            else :
                print(0,end="")
        print()

