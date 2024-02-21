# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n, m, k = map(int,input().split())
        sticker = dict()
        for idx in range(k) :
            tn, tm = map(int,input().split())
            sticker[idx] = list(list(map(int,input().split())) for _ in range(tn))
            sticker[idx].append([tn,tm])
        board = list(list(0 for _ in range(m)) for _ in range(n))
        return n, m, k, sticker, board

    n, m, k, sticker, board = getdata()

    def printboard(board) :
        for row in board :
            print(row)

    def printsticker(sticker) :
        for idx, row in enumerate(sticker) :
            if idx == len(sticker)-1 :
                break
            print(row)

    def canattach(x, y, board, sticker) :
        tn, tm = sticker[-1][0], sticker[-1][1]
        if x+tn > len(board) or y+tm > len(board[0]) :
            return False
        for i in range(tn) :
            for j in range(tm) :
                if board[x+i][y+j] == 1 and sticker[i][j] == 1:
                    return False
        return True

    def attach(x, y, board, sticker) :
        tn, tm = sticker[-1][0], sticker[-1][1]
        for i in range(tn):
            for j in range(tm):
                if sticker[i][j] == 1:
                    board[x+i][y+j] = 1
        return board

    def boardattach(board, sticker) :
        for i in range(n) :
            for j in range(m) :
                if canattach(i,j,board,sticker) :
                    # print(i, j)
                    attach(i,j,board,sticker)
                    return board, True
        return board, False

    def spinsticker(sticker) :
        tn, tm = sticker[-1][0], sticker[-1][1]
        res = list(list(0 for _ in range(tn)) for _ in range(tm))
        for i in range(tm) :
            for j in range(tn) :
                if sticker[tn-j-1][i] == 1:
                    res[i][j] = 1
        res.append([tm, tn])
        return res

    def countboard(board) :
        cnt = 0
        for row in board :
            cnt += row.count(1)
        return cnt

    def sol(board) :
        for ts in sticker :
            # print(f"==={ts}th sticker===")
            cnt = 0
            copy_s = sticker[ts]
            while True :
                board, flag = boardattach(board, copy_s)
                if flag :
                    break
                else :
                    cnt += 1
                    if cnt == 4 :
                        break
                    copy_s = spinsticker(copy_s)
            # printsticker(copy_s)
            # print(copy_s[-1])
        # printboard(board)
        print(countboard(board))

    sol(board)