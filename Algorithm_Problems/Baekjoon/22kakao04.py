from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    gp = defaultdict(list)
    for p in paths:
        gp[p[0]].append((p[1], p[2]))
    print(gp)
    need_visited = list()
    intensity = list(float('inf') for _ in range(n+1))
    for g in gates:
        heapq.heappush(need_visited, (0, g))
        intensity[g] = 0
    while need_visited:
        weight, node = heapq.heappop(need_visited)
        if node in summits or weight > intensity[node]:
            continue
        for next_node, next_weight in gp[node]:
            inten = max(weight, next_weight)
            if inten < intensity[next_node]:
                intensity[next_node] = inten
                heapq.heappush(need_visited, (intensity[next_node], next_node))
    answer = list()
    for s in summits:
        heapq.heappush(answer, (intensity[s], s))
    return list(answer[0])