# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(list(map(int, input().split())) for _ in range(n))
        return n, board

    n, board = getdata()
    green = list(list(0 for _ in range(4)) for _ in range(6))
    blue = list(list(0 for _ in range(4)) for _ in range(6))

    def getblock(color, loc, dt, fl) :
        flag = 0
        if  fl == 1:
            if dt == 2 :
                dt = 3
            elif dt == 3:
                dt = 2
        for i in range(6) :
            if dt == 2 :
                if color[i][loc] == 1 or color[i][loc+1] == 1:
                    flag = 1
                    color[i-1][loc], color[i-1][loc+1] = 1, 1
                    break
            else :
                if color[i][loc] == 1 :
                    flag = 1
                    if dt == 1 :
                        color[i-1][loc] = 1
                    elif dt == 3 :
                        color[i-1][loc], color[i-2][loc] = 1, 1
                    break
        if flag == 0:
            if dt == 1 :
                color[5][loc] = 1
            elif dt == 2:
                color[5][loc], color[5][loc+1] = 1, 1
            else :
                color[5][loc], color[4][loc] = 1, 1
        return color

    def printboard(board) :
        for row in board :
            print(row)

    def dfs(color, visited, x, y) :
        visited.append([x,y])
        if 0<=x-1 and color[x-1][y] == 1 and [x-1,y] not in visited:
            dfs(color, visited, x-1, y)
        if 0<=y-1 and color[x][y-1] == 1 and [x,y-1] not in visited :
            dfs(color, visited, x, y-1)
        if x+1 <= 5 and color[x+1][y] == 1 and [x+1,y] not in visited:
            dfs(color, visited, x+1, y)
        if y+1 <= 5 and color[x][y+1] == 1 and [x,y+1] not in visited:
            dfs(color, visited, x, y+1)

    def checkbottom(color) :
        blk = list()
        visited=list()
        for i in range(6) :
            for j in range(4) :
                if color[i][j] == 1 and [i,j] not in visited:
                    tmp = list()
                    dfs(color,tmp,i,j)
                    blk.append(tmp)
                    visited.extend(tmp)
        return blk

    def blockdown(color, row) :
        for i in range(row, 0, -1) :
            color[i] = color[i-1]
        color[0] = [0, 0, 0, 0]
        blk = checkbottom(color)
        for block in blk :
            flag = 0
            for bl in block :
                if bl[0] == 5 :
                    flag = 1
            if flag == 0:
                for bl in block :
                    color[bl[0]][bl[1]] = 0
                    color[bl[0]+1][bl[1]] = 1

        return color

    def getscore(color) :
        res = 0
        for idx, row in enumerate(color) :
            if row.count(1) == 4 :
                res += 1
                color = blockdown(color, idx)
        return res

    def checkrow(color) :
        while color[1].count(0) != 4 :
            blockdown(color, 5)

    def countblock(color) :
        cnt = 0
        for row in color :
            cnt += row.count(1)
        return cnt

    def sol(board, green, blue) :
        res = 0
        ind = 1
        for block in board :
            print(f"===={ind}th block====")
            dt, x, y = block[0], block[1], block[2]
            green = getblock(green, y, dt, 0)
            blue = getblock(blue, x, dt, 1)
            while True :
                res += getscore(green)
                res += getscore(blue)
                checkrow(green)
                checkrow(blue)
            printboard(green)
            print(f"-score={res}")
            printboard(blue)
            ind += 1
        print(res)
        print(countblock(green)+countblock(blue))

    sol(board, green, blue)