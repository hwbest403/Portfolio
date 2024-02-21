# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    for j in range(1,n) :
        print(f"=={j}==")
        res = list(0 for _ in range(10))
        for i in range(1,j+1) :
            t = str(i)
            for l in t :
                res[int(l)] += 1
        print(*res)
