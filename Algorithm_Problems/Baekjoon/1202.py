# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    import heapq

    def getdata():
        n, k = map(int,input().split())
        stuff = list()
        for _ in range(n) :
            heapq.heappush(stuff, list(map(int,input().split())))
        knap = list()
        for _ in range(k) :
            heapq.heappush(knap,int(input()))
        return n, k, stuff, knap

    # 각 가방의 무게 한계에 맞게 가장 값진 보석을 넣어야 함
    # 1. min heap으로 정렬된 knap에서 하나 꺼냄 -> 무게 한계가 가장 작은 가방(logK)
    # 2. 해당 가방의 무게 한계보다 무게가 작은 보석을 새로운 max heap에 저장(보석 제외 -> logN, 보석 추가 -> logN)
    # 3. 이후 max heap에서 하나를 꺼냄 (logN)
    def sol(stuff, knap):
        result = 0
        Max_heap = list()
        while knap :
            item = heapq.heappop(knap) # 1번
            while stuff and stuff[0][0] <= item :
                tmp = heapq.heappop(stuff)[1] # 2번 보석 삭제
                heapq.heappush(Max_heap,-tmp) # 2번 maxheap에 추가
            if Max_heap :
                result += -heapq.heappop(Max_heap) # 3번
            elif not stuff :
                break
        return result

    n, k, stuff, knap = getdata()
    print(sol(stuff, knap))
