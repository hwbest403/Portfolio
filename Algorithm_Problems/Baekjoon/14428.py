# coding = utf-8
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
tmp = list(map(int,input().split()))
ls = list()
for idx, num in enumerate(tmp) :
    ls.append([num, idx+1])
SegT = list([INF,INF] for _ in range(n*4))

def min(a, b) :
    if a[0] > b[0] :
        return b
    else :
        return a

def MakeTree(tree, node, start, end) :
    if start == end :
        tree[node] = ls[start]
        return tree[node]
    else :
        tree[node] = min(MakeTree(tree, node*2+1, start, (start+end)//2),MakeTree(tree, node*2+2, (start+end)//2+1, end))
        return tree[node]

MakeTree(SegT, 0, 0, n-1)

def UpdateTree(tree, node, start, end, target, value) :
    if target<start or end<target :
        return
    if start == end and start == target :
        tree[node] = [value, target+1]
        return
    UpdateTree(tree, node*2+1, start, (start+end)//2, target, value)
    UpdateTree(tree, node*2+2, (start+end)//2+1, end, target, value)
    tree[node] = min(tree[node*2+1], tree[node*2+2])

def FindTree(tree, node, start, end, left, right) :
    if end<left or right<start :
        return [INF, INF]
    if left<=start and end<=right :
        return tree[node]
    return min(FindTree(tree, node*2+1, start, (start+end)//2, left, right), FindTree(tree, node*2+2, (start+end)//2+1, end, left, right))

for _ in range(int(input())) :
    a, b, c = map(int,input().split())
    if a == 1 :
        # print(b, c)
        ls[b-1] = [c, b]
        # print(ls)
        UpdateTree(SegT, 0, 0, n-1, b-1, c)
        # print(SegT)
    else :
        print(FindTree(SegT, 0, 0, n-1, b-1, c-1)[1])