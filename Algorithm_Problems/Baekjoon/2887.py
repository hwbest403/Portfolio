# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    import heapq


    def getdata():
        n = int(input())
        board = list()
        for i in range(n) :
            tmp=list(map(int,input().split()))
            tmp.append(i)
            board.append(tmp)
        return n, board

    n, board = getdata()
    par=list(i for i in range(n))
    hq = list()

    # 문제의 요구사항인 min(좌표들) 에서 x, y, z로 각각 나누어 보면
    # 여느 두 정점 사이 다른 정점이 있을 경우 해당 두 정점을 이어주는 간선은
    # MST를 구성할 수 있는 간선이 아님
    # EX) x좌표 기준 a: 10, b: 12, c: 14
    # a와 b를 이어주는 간선은 a-b, b-c로 최소 비용으로 최대 정점을 연결할 수 있음
    # 밑의 코드는 문제에 주어진 정점을 통해 유효한 간선을 선택하고 heap에 저장
    for i in range(3) :
        board.sort(key=lambda x:x[i],reverse = False)
        for j in range(1, n) :
            heapq.heappush(hq,(board[j][i]-board[j-1][i], board[j][3], board[j-1][3]))

    # 크루스칼 알고리즘을 위한 유니온 파인드
    def find(a) :
        if a == par[a] :
            return a
        else :
            return find(par[a])

    def union(a, b) :
        a, b = find(a), find(b)
        if a>b :
            par[a] = b
        else :
            par[b] = a

    total_weight = 0
    while hq :
        tmp = heapq.heappop(hq)
        w, lv, rv = tmp[0],tmp[1],tmp[2]
        if find(lv) != find(rv) :
            union(lv, rv)
            total_weight += w
    print(total_weight)