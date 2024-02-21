# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n, m = map(int,input().split())
        shark = list()
        for idx in range(n) :
            tmp = list(map(int,input().split()))
            for i in range(m) :
                if tmp[i] == 1 :
                    shark.append([idx,i])
        return n, m, shark

    n, m, shark = getdata()
    res = 0
    for i in range(n) :
        for j in range(m) :
            mind = 10**3
            for s in shark :
                dis = min(abs(s[0]-i),abs(s[1]-j))+abs(abs(s[0]-i)-abs(s[1]-j))
                if dis<mind :
                    mind = dis
            if mind > res :
                res = mind
    print(res)