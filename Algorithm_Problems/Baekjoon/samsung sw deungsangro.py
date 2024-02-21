import sys
input = sys.stdin.readline

def getdata():
    n, k = map(int,input().split())
    board = list(list(map(int,input().split())) for _ in range(n))
    return n, k, board

def dfs(board, visited, i, j, h, d, k, flag, dx, dy, inrange, test_case):
    # if test_case == 6:
    #     print(i, j, d, h)
    global tmp
    tmp = max(d, tmp)
    for dir in range(4):
        nx, ny = i+dx[dir], j+dy[dir]
        if inrange(nx, ny) and not visited[ny][nx]:
            if board[nx][ny] < h:
                visited[nx][ny] = True
                dfs(board, visited, nx, ny, board[nx][ny], d + 1, k, flag, dx, dy, inrange, test_case)
                visited[nx][ny] = False
            else:
                if not flag and board[nx][ny] - k < h:
                    visited[nx][ny] = True
                    dfs(board, visited, nx, ny, h-1, d + 1, k, True, dx, dy, inrange, test_case)
                    visited[nx][ny] = False

def sol(test_case):
    n, k, board = getdata()
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    inrange = lambda x, y: 0<=x<n and 0<=y<n
    visited = list(list(False for _ in range(n)) for _ in range(n))
    max_h = -1
    answer = 0
    for i in range(n):
        for j in range(n):
            max_h = max(max_h, board[i][j])
    for i in range(n):
        for j in range(n):
            if board[i][j] == max_h:
                global tmp
                tmp = 0
                visited[i][j] = True
                # if test_case == 6:
                #     print(f"#{i},{j}")
                dfs(board, visited, i, j, board[i][j], 1, k, False, dx, dy, inrange, test_case)
                visited[i][j] = False
                answer = max(tmp, answer)
    return answer

T = int(input())
for test_case in range(1, T+1):
    answer = sol(test_case)
    print(f"#{test_case} {answer}")