# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n, m, k = map(int,input().split())
        board = list(map(int, input().split()))
        chul = list(map(int,input().split()))
        return n, m, k, board, chul

    n, m, k, board, chul = getdata()
    for idx, num in enumerate(board) :
        board[idx] = [num, 0]
    board.sort(key=lambda x:x[0], reverse=False)

    def binary_search(board, k) :
        s, e = 0, len(board)-1
        while s<e :
            if board[s][1] == 1 :
                s+=1
                continue
            if board[e][1] == 1:
                e-=1
                continue
            mid = (s+e)//2
            if board[mid][0] <= k :
                s = mid+1
            else :
                e = mid
        return s

    for num in chul :
        tmp = binary_search(board, num)
        board[tmp][1] = 1
        print(board[tmp][0])