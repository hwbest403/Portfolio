# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque

    def getdata():
        n, m = map(int,input().split())
        board = list(list(map(int, input().rstrip())) for _ in range(n))
        return n, m, board

    n, m, board = getdata()
    need_visited, visited = deque(), dict()
    need_visited.append([0,0])
    visited[0,0] = 1
    while need_visited :
        print(need_visited)
        nxt = need_visited.popleft()
        nx, ny = nxt[0], nxt[1]
        if nx == n-1 and ny == m :
            break
        if 0<=nx-1 and board[nx-1][ny] == 1 and (nx-1, ny) not in visited :
            need_visited.append([nx-1,ny])
            visited[nx-1, ny] = visited[nx, ny] + 1
        if 0<=ny-1 and board[nx][ny-1] == 1 and (nx, ny-1) not in visited :
            need_visited.append([nx,ny-1])
            visited[nx, ny-1] = visited[nx, ny] + 1
        if nx+1<n and board[nx+1][ny] == 1 and (nx+1, ny) not in visited :
            need_visited.append([nx+1,ny])
            visited[nx+1, ny] = visited[nx, ny] + 1
        if ny+1<m and board[nx][ny+1] == 1 and (nx, ny+1) not in visited :
            need_visited.append([nx,ny+1])
            visited[nx, ny+1] = visited[nx, ny] + 1
    print(visited)
    print(visited[n-1, m-1])