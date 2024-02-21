if __name__ == '__main__' :
    import sys
    input = sys.stdin.readline
    from collections import deque

    n = int(input())
    board = list(int(input()) for _ in range(n))
    graph = dict()
    for i in range(n) :
        graph[i+1] = board[i]
    ans = list()
    for i in range(1, n+1) :
        cur = i
        if cur not in ans :
            tmp = list()
            for _ in range(n) :
                next = graph[cur]
                tmp.append(next)
                if next == i :
                    ans.extend(tmp)
                    break
                else :
                    cur = next
    print(len(ans))
    ans.sort(reverse=False)
    for i in range(len(ans)):
        print(ans[i])