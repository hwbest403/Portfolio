# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(map(int, input().split()))
        return n, board

    n, board = getdata()
    board.sort(reverse=False)

    def power(a,b) :
        res = 1
        while b>0 :
            if b%2 != 0 :
                res = (res*a)
            b //= 2
            a = (a*a)
        return res%1000000007

    res = 0
    for i in range(n) :
        res += board[i] * (power(2,i)-power(2,n-i-1))
    print(res%1000)