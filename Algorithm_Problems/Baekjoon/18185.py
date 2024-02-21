# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(map(int, input().split()))
        return n, board

    n, board = getdata()
    res = 0
    # idx = 0
    while board :
        # print(f"==={idx}")
        # print(board)
        # print(res)
        # idx += 1
        flag = 0
        while board[0] == 0 :
            del board[0]
            if not board :
                flag = 1
                break
        if flag == 1:
            break
        if len(board) > 2 :
            if board[1] == 0 :
                res += board[0]*3
                board[0] = 0
            elif board[2] == 0 :
                minv = min(board[0:2])
                res += minv * 5
                board[0] -= minv
                board[1] -= minv
                maxv = max(board[0:2])
                res += maxv * 3
                board[0], board[1] = 0, 0
            else :
                minv = min(board[0:3])
                if board[1] <= board[2] :
                    res += minv*7
                    board[0] -= minv
                    board[1] -= minv
                    board[2] -= minv
                else :
                    minv = min(board[0], board[1]-board[2])
                    res += minv*5
                    board[0] -= minv
                    board[1] -= minv
        elif len(board) > 1 :
            minv = min(board[0:2])
            res += minv*5
            board[0] -= minv
            board[1] -= minv
            maxv = max(board[0:2])
            res += maxv*3
            board[0],board[1] = 0, 0
        else :
            res += board[0]*3
            board[0] = 0
    print(res)