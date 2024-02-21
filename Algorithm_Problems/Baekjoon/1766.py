# coding = utf-8

if __name__ == '__main__':
    import sys
    import heapq
    input = sys.stdin.readline

    def getdata():
        n, m = map(int,input().split())
        return n, m

    hq = list()
    n, m = getdata()
    iflag = list(0 for _ in range(n))
    edge = list(0 for _ in range(m))
    for i in range(m) :
        tmp = list(map(int, input().split()))
        edge[i]=tmp
        iflag[tmp[1]-1] += 1
    for i in range(n) :
        if iflag[i] == 0 :
            heapq.heappush(hq,i+1)
            iflag[i] -= 1
    while hq :
        tmp = heapq.heappop(hq)
        print(tmp, end=" ")
        for e in edge :
            if e[0] == tmp :
                iflag[e[1]-1] -= 1
        for i in range(n):
            if iflag[i] == 0:
                heapq.heappush(hq, i + 1)
                iflag[i] -= 1
