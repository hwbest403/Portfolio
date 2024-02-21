# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m, k = map(int,input().split())
    ls = list()
    for _ in range(n) :
        ls.append(int(input()))

    MOD = 1000000007
    SegT = list(0 for _ in range(n*4))

    def MakeTree(tree, node, start, end) :
        if start == end :
            tree[node] = ls[start]
            return tree[node]
        else :
            tree[node] = (MakeTree(tree, node*2+1, start, (start+end)//2) * MakeTree(tree, node*2+2, (start+end)//2+1, end)) % MOD
            return tree[node]

    MakeTree(SegT, 0, 0, n-1)
    # print(SegT)

    def UpdateTree(tree, node, start, end, target, prev_val, next_val) :
        if target<start or end<target :
            return tree[node]
        elif start == end :
            tree[node] = next_val
            return tree[node]
        tree[node] = (UpdateTree(tree, node*2+1, start, (start+end)//2, target, prev_val, next_val) * UpdateTree(tree, node*2+2, (start+end)//2+1, end, target, prev_val, next_val)) % MOD
        return tree[node]

    def FindTree(tree, node, start, end, left, right) :
        if end<left or right<start :
            return 1
        if left<=start and end<=right :
            return tree[node]
        return FindTree(tree, node*2+1, start, (start+end)//2, left, right) * FindTree(tree, node*2+2, (start+end)//2+1, end, left, right)

    for _ in range(m+k) :
        a, b, c = map(int,input().split())
        if a == 1 :
            UpdateTree(SegT, 0, 0, n-1, b-1, ls[b-1], c)
            ls[b-1] = c
        else :
            print(FindTree(SegT, 0, 0, n-1, b-1, c-1)%MOD)
