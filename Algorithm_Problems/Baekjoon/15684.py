# coding = utf-8

import sys
input = sys.stdin.readline

n, m, h = map(int,input().split())
visited = list(list(-1 for _ in range(h)) for _ in range(n-1))

for _ in range(m) :
    a, b = map(int,input().split())
    visited[b-1][a-1] = 1
    if b-2 >= 0 :
        visited[b-2][a-1] = 0
    if b < n-1 :
        visited[b][a-1] = 0

def check() :
    for i in range(n) :
        t_idx = i
        for j in range(h) :
            tmp = set()
            if t_idx - 1 >= 0:
                tmp.add(t_idx - 1)
            if t_idx < n - 1:
                tmp.add(t_idx)
            for t in tmp :
                if visited[t][j] == 1 :
                    if t<t_idx :
                        t_idx -= 1
                        break
                    else :
                        t_idx += 1
                        break
        if t_idx != i :
            return False
    return True


def sol(k, l) :
    if k == l :
        b = check()
        if b :
            print(l)
            sys.exit()
        return b

    for i in range(n-1) :
        for j in range(h) :
            if visited[i][j] == -1 :
                visited[i][j] = 1
                if i - 1 >= 0:
                    visited[i-1][j] = 0
                if i + 1 < n-1 :
                    visited[i+1][j] = 0
                sol(k+1, l)
                visited[i][j] = -1
                if i - 1 >= 0:
                    if i - 2 >= 0 :
                        if visited[i-2][j] == 1 :
                            visited[i - 1][j] = 0
                        else :
                            visited[i-1][j] = -1
                    else :
                        visited[i-1][j] = -1
                if i + 1 < n-1 :
                    if i + 2 < n-1 :
                        if visited[i+2][j] == 1 :
                            visited[i + 1][j] = 0
                        else :
                            visited[i + 1][j] = -1
                    else :
                        visited[i+1][j] = -1

for i in range(4) :
    sol(0, i)
print(-1)