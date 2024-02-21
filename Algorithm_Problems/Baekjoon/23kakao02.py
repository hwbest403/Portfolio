from collections import defaultdict

def solution(edges):
    # initialize
    gp = defaultdict(list)
    node = set()
    for e in edges:
        gp[e[0]].append(e[1])
        node.add(e[0])
        node.add(e[1])
    graph_idx = defaultdict(list)
    need_visited = list()
    visited = list(-1 for _ in range(len(node)+1))
    idx = 0
    for i in range(1, len(node)+1):
        if visited[i] == -1:
            tmp_gp = set()
            need_visited.append(i)
            while need_visited:
                tmp_node = need_visited.pop()
                tmp_gp.add(tmp_node)
                visited[tmp_node] = idx
                for next_node in gp[tmp_node]:
                    if visited[next_node] == -1:
                        need_visited.append(next_node)
        idx += 1
    answer = []
    return answer