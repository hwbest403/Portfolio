from collections import deque, defaultdict

n, m, v = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(m))
graph = defaultdict(list)

def bfs(graph, v):
    for e in board:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    for i in range(1, n + 1):
        graph[i].sort()
    need_visited, visited = deque(), deque()
    need_visited.append(v)
    while need_visited:
        node = need_visited.popleft()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

def dfs(graph, v):
    for e in board:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    for i in range(1, n + 1):
        graph[i].sort(reverse=True)

    need_visited, visited = deque(), deque()
    need_visited.append(v)

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

print(*dfs(graph, v))
print(*bfs(graph, v))