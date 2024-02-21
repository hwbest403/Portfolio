# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        l = int(input())
        ml, mk = map(int,input().split())
        c = int(input())
        board = list()
        for _ in range(l) :
            tmp = int(input())
            board.append([tmp,0])
        return l, ml, mk, c, board

    l, ml, mk, c, board = getdata()
    snum = 0
    for i in range(l) :
        if i>=ml :
            if board[i-ml][1] == 0 :
                snum -= 1
        if board[i][0] > (snum+1)*mk :
            if c > 0 :
                c -= 1
                board[i][1] = 1
            else :
                print("NO")
                sys.exit()
        else :
            snum += 1
    print("YES")