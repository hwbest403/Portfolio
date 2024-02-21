# https://www.acmicpc.net/problem/1063

if __name__ == '__main__' :
    import sys
    input = sys.stdin.readline

    k, r, n = list(input().split())
    # R L B T RT LT RB LB
    dx = [0,0,1,-1,-1,-1,1,1]
    dy = [1,-1,0,0,1,-1,1,-1]
    kx, ky = 8-int(k[1]), ord(k[0])-65
    rx, ry = 8-int(r[1]), ord(r[0])-65
    for _ in range(int(n)) :
        command = input().rstrip()
        if command == 'R' :
            command = 0
        if command == 'L' :
            command = 1
        if command == 'B' :
            command = 2
        if command == 'T' :
            command = 3
        if command == 'RT' :
            command = 4
        if command == 'LT' :
            command = 5
        if command == 'RB' :
            command = 6
        if command == 'LB' :
            command = 7
        nkx, nky = kx+dx[command], ky+dy[command]
        if 0<=nkx<8 and 0<=nky<8 :
            kx, ky = nkx, nky
        else :
            kx, ky = nkx-dx[command], nky-dy[command]
        if kx == rx and ky == ry :
            nrx, nry = rx+dx[command], ry+dy[command]
            if 0 <= nrx < 8 and 0 <= nry < 8:
                rx, ry = nrx, nry
            else:
                rx, ry = nrx - dx[command], nry - dy[command]
                kx, ky = nkx - dx[command], nky - dy[command]

    kx, rx = 8-kx, 8-rx
    ky, ry = chr(ky+65), chr(ry+65)
    print(ky, end="")
    print(kx)
    print(ry, end="")
    print(rx)