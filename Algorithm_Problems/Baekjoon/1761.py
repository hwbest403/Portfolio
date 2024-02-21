# coding = utf-8

if __name__ == '__main__':
    import sys
    from collections import defaultdict
    input = sys.stdin.readline

    n = int(input())

    tree = defaultdict(list)
    parent = list(list(0 for _ in range(21)) for _ in range(n+1))
    depth = list(0 for _ in range(n+1))
    dp = list(0 for _ in range(n+1))

    for _ in range(n-1) :
        lv, rv, w = map(int,input().split())
        tree[lv].append((rv,w))
        tree[rv].append((lv,w))

    depth[0] = -1

    def printparent() :
        for row in parent :
            print(row)

    def dfs(tree) :
        need_visited, visited = list(), list()
        need_visited.append(1)
        while need_visited :
            next = need_visited.pop()
            if next not in visited :
                visited.append(next)
                for item in tree[next] :
                    if item[0] not in visited :
                        need_visited.append(item[0])
                        parent[item[0]][0] = next
                        depth[item[0]] = depth[next] + 1
                        dp[item[0]] += dp[next] + item[1]

    dfs(tree)

    def set_par() :
        for i in range(1, 21) :
            for j in range(1, n+1) :
                parent[j][i] = parent[parent[j][i-1]][i-1]

    set_par()

    def LCA(lv, rv) :
        if depth[lv] > depth[rv] :
            lv, rv = rv, lv
        for i in range(20, -1, -1) :
            if depth[rv] - depth[lv] >= (1<<i) :
                rv=parent[rv][i]
        if lv == rv :
            return lv
        for i in range(20,-1,-1) :
            if parent[lv][i] != parent[rv][i] :
                lv = parent[lv][i]
                rv = parent[rv][i]
        return parent[lv][0]

    m = int(input())
    for _ in range(m) :
        lv, rv = map(int,input().split())
        print(dp[lv]+dp[rv]-2*dp[LCA(lv,rv)])