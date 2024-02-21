# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    ls = list(map(int,input().split()))
    res = list()
    for idx, val in enumerate(ls) :
        tmp = list()
        for _ in range(val) :
            if res :
                tmp.append(res.pop())
        res.append(idx+1)
        while tmp :
            res.append(tmp.pop())
    print(*res)
