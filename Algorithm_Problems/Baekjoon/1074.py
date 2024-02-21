# https://www.acmicpc.net/problem/1074

if __name__ == '__main__' :
    import sys
    input = sys.stdin.readline

    n, r, c = list(map(int,input().split()))
    ans = 0
    def search(n, tr, tc, cnt):
        global ans
        if n == 1:
            ans = cnt + (r - tr) * 2 +  (c - tc)
            return
        split = (2 ** (n - 1))
        square = split ** 2
        if tr <= r < tr + split and tc <= c < tc + split:
            search(n-1, tr, tc, cnt)
        elif tr <= r < tr + split and tc + split <= c < tc + 2 * split:
            search(n-1, tr, tc+split, cnt + square)
        elif tr + split <= r < tr + 2 * split and tc <= c < tc + split:
            search(n-1, tr+split, tc, cnt + 2 * square)
        else:
            search(n-1, tr+split,tc+split, cnt + 3 * square)

    search(n, 0, 0, 0)
    print(ans)

