if __name__ == '__main__' :
    import sys
    input = sys.stdin.readline
    from collections import deque

    board = list(list(map(int,input().split())) for _ in range(4))
    visited = deque()
    for i in range(4) :
        sx, sy, ex, ey = board[i][0], board[i][1], board[i][2], board[i][3]
        for j in range(sx, ex) :
            for k in range(sy, ey) :
                if j*100+k not in visited :
                    visited.append(j*100+k)
    print(len(visited))