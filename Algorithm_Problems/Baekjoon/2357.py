# coding = utf-8

if __name__ == '__main__':
    import sys
    from heapq import *
    input = sys.stdin.readline

    n, m = map(int,input().split())
    ls = list()
    min_segt, max_segt = list(10**10 for _ in range(n*4)), list(0 for _ in range(n*4))

    for _ in range(n) :
        ls.append(int(input()))

    # print(ls)

    def makemaxtree(tree, node, start, end) :
        if start == end :
            tree[node] = ls[start]
            return tree[node]
        else :
            tree[node] = max(makemaxtree(tree, node*2+1, start, (start+end)//2), makemaxtree(tree, node*2+2, (start+end)//2+1, end))
            return tree[node]

    def makemintree(tree, node, start, end) :
        if start == end :
            tree[node] = ls[start]
            return tree[node]
        else :
            tree[node] = min(makemintree(tree, node*2+1, start, (start+end)//2), makemintree(tree, node*2+2, (start+end)//2+1, end))
            return tree[node]

    makemaxtree(max_segt, 0, 0, n-1)
    makemintree(min_segt, 0, 0, n-1)
    # print(max_segt)
    # print(min_segt)

    def findmax(tree, node, start, end, left, right) :
        if left>end or right<start :
            return 0
        if left<=start and end<=right :
            return tree[node]
        return max(findmax(tree, node*2+1, start, (start+end)//2, left, right), findmax(tree, node*2+2, (start+end)//2+1, end, left, right))

    def findmin(tree, node, start, end, left, right) :
        if left>end or right<start :
            return 10**10
        if left<=start and end<=right :
            return tree[node]
        return min(findmin(tree, node*2+1, start, (start+end)//2, left, right), findmin(tree, node*2+2, (start+end)//2+1, end, left, right))

    for _ in range(m) :
        a, b = map(int,input().split())
        print(findmin(min_segt, 0, 0, n-1, a-1, b-1), findmax(max_segt, 0, 0, n-1, a-1, b-1))