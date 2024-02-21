# coding = utf-8

import sys
input = sys.stdin.readline
import heapq
from collections import deque

n, k = map(int, input().split())

def sol(n, k):
    need_visited, visited = deque(), list()
    result = list()
    need_visited.append((n, 0))
    while need_visited:
        node = need_visited.popleft()
        num, count = node[0], node[1]
        if count == k:
            heapq.heappush(result, -num)
        if count == k+1:
            if not result:
                return -1
            return -result[0]
        if (num, count) not in visited:
            visited.append((num, count))
            for i in range(len(str(num))-1):
                for j in range(i+1, len(str(num))):
                    num_ls = list(str(num))
                    if i == 0 and num_ls[j] == '0':
                        continue
                    num_ls[i], num_ls[j] = num_ls[j], num_ls[i]
                    n_num = int(''.join(num_ls))
                    need_visited.append((n_num, count+1))
    if not result:
        return -1
    return -result[0]

print(sol(n, k))