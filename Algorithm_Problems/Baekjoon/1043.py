# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque

    def getdata():
        n, m = map(int,input().split())
        board = list()
        know = list(map(int,input().split()))
        del know[0]
        for i in range(m) :
            tmp = list(map(int,input().split()))
            del tmp[0]
            board.append(tmp)
        return n, m, board, know

    n, m, board, know = getdata()

    if len(know) == 0 :
        print(m)
    else :
        visited = list()
        while know :
            node = know.pop()
            if node not in visited :
                visited.append(node)
                for i in board :
                    if node in i :
                        know.extend(i)
        cnt = 0
        for i in range(m):
            flag = 0
            for j in range(len(visited)):
                if visited[j] in board[i]:
                    flag = 1
                    break
            if flag == 0:
                cnt += 1
        print(cnt)