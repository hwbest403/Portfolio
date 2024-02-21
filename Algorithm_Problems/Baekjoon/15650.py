# coding = utf-8

if __name__ == '__main__':
    import sys
    from itertools import combinations
    input = sys.stdin.readline

    def getdata():
        n, m = map(int,input().split())
        return n, m

    n, m = getdata()
    for case in combinations([i+1 for i in range(n)], m) :
        print(*case)