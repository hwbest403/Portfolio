if __name__ == '__main__' :
    import sys
    import copy
    input = sys.stdin.readline

    n = int(input())
    want = list(list(map(int,input().split())) for _ in range(n*n))
    board = [[0]*n for _ in range(n)]

    def printboard(board) :
        for i in range(n) :
            print(board[i])
        return

    def stuin(want, board) :
        info = [[-1]*n for _ in range(n)]
        blank = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n) :
                if board[i][j] == 0:
                    info[i][j] = 0
                    if i-1 >= 0 and board[i-1][j] in want :
                        info[i][j] += 1
                    if i-1 >= 0 and board[i-1][j] == 0 :
                        blank[i][j] += 1
                    if j-1 >= 0 and board[i][j-1] in want :
                        info[i][j] += 1
                    if j-1 >= 0 and board[i][j-1] == 0 :
                        blank[i][j] += 1
                    if i+1 < n and board[i+1][j] in want :
                        info[i][j] += 1
                    if i+1 < n and board[i+1][j] == 0 :
                        blank[i][j] += 1
                    if j+1 < n and board[i][j+1] in want :
                        info[i][j] += 1
                    if j+1 < n and board[i][j+1] == 0 :
                        blank[i][j] += 1
        maxind = list()
        tmp = -1
        for i in range(n) :
            if max(info[i]) > tmp :
                tmp = max(info[i])
        for i in range(n) :
            for j in range(n) :
                if info[i][j] == tmp :
                    maxind.append([i,j])
        if len(maxind) == 1:
            board[maxind[0][0]][maxind[0][1]] = want[0]
            return
        maxind2 = list()
        tmp = -1
        for i in range(len(maxind)) :
            if blank[maxind[i][0]][maxind[i][1]] > tmp :
                tmp = blank[maxind[i][0]][maxind[i][1]]
                if len(maxind2) == 0 :
                    maxind2.append(maxind[i])
                else :
                    while maxind2 :
                        maxind2.pop()
                    maxind2.append(maxind[i])
            elif blank[maxind[i][0]][maxind[i][1]] == tmp :
                maxind2.append(maxind[i])
        board[maxind2[0][0]][maxind2[0][1]] = want[0]
        return

    def score(want, board) :
        result = 0
        for i in range(n) :
            for j in range(n) :
                cnt = 0
                tmp = board[i][j]
                for k in range(len(want)) :
                    if tmp == want[k][0] :
                        tmpind = k
                        break
                if i - 1 >= 0 and board[i - 1][j] in want[tmpind]:
                    cnt += 1
                if j - 1 >= 0 and board[i][j - 1] in want[tmpind]:
                    cnt += 1
                if i + 1 < n and board[i + 1][j] in want[tmpind]:
                    cnt += 1
                if j + 1 < n and board[i][j + 1] in want[tmpind]:
                    cnt += 1
                if cnt == 1 :
                    result += 1
                if cnt == 2 :
                    result += 10
                if cnt == 3 :
                    result += 100
                if cnt == 4 :
                    result += 1000
        return result

    def sol(want, board) :
        copy_board = copy.deepcopy(board)
        for i in range(n*n) :
            #print(f"==={i}th===")
            #print(want[i])
            stuin(want[i],copy_board)
            #printboard(copy_board)
        result = score(want,copy_board)
        return result

    print(sol(want, board))