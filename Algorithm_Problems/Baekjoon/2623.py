if __name__ == '__main__':
    import sys
    from collections import deque
    input = sys.stdin.readline

    n,m = map(int,input().split())
    board = list(list(map(int,input().split())) for _ in range(m))

    flag = list(0 for _ in range(n))
    edge = list()
    for i in range(m) :
        for j in  range(1, len(board[i])) :
            if j != 1 :
                flag[board[i][j]-1] += 1
            edge.append((board[i][j-1]-1,board[i][j]-1))

    res = deque()
    for i in range(n) :
        if flag[i] == 0:
            res.append(i)
            flag[i] -= 1

    ans = deque()
    while res :
        tmp = res.popleft()
        ans.append(tmp+1)
        for arr in edge :
            if arr[0] == tmp :
                flag[arr[1]] -= 1
        for i in range(n):
            if flag[i] == 0:
                res.append(i)
                flag[i] -= 1
    if sum(flag) > 0 :
        print(0)
    else :
        for i in ans:
            print(i)