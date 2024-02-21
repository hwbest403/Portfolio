# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    l = int(input())
    n = int(input())
    command = list()
    for idx in range(n):
        tmp = list(input().rstrip().split())
        tmp[0] = int(tmp[0])
        if idx != 0:
            tmp[0] += command[-1][0]
        command.append(tmp)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def move(x, y, dir) :
        nx = x+dx[dir]
        ny = y+dy[dir]
        return nx, ny

    snake = list()
    sx, sy = 0, 0
    snake.append([sx,sy])
    dir = 1

    while True :
        dis = 0
        tx, ty = snake[-1][0], snake[-1][1]
        while True :
            tx, ty = move(tx, ty, dir)
            break
        break
