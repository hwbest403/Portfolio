# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        tree = list(list() for _ in range(n+1))
        for _ in range(n-1) :
            u, v = map(int,input().split())
            tree[u].append(v)
            tree[v].append(u)
        return n, tree

    n, tree = getdata()
    leaf = list()
    for i in range(n+1) :
        if len(tree[i]) == 1:
            leaf.append(i)
    print(tree)
    print(leaf)
    visited = list(0 for _ in range(n+1))
    while leaf :
        tmp = leaf.pop()
        if len(tree[tmp]) == 0:
            continue
        par = tree[tmp][0]
        visited[par] = 1
        for i in tree[par] :
            tree[i].remove(par)
            if len(tree[i]) == 1:
                leaf.append(i)
        visited[par] = 1
        tree[par] = list()
    print(sum(visited))