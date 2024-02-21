# coding = utf-8

import sys
input = sys.stdin.readline

class node:
    def __init__(self, value):
        self.value = value
        self.child = [None for _ in range(10)]

class trie:
    def __init__(self):
        self.root = node('')

    def push(self, s):
        t = self.root
        for idx, c in enumerate(s):
            if t.child[c] is not None:
                if idx == len(s)-1:
                    return False
                t = t.child[c]
                if t.child.count(None) == 10:
                    return False
            else:
                n = node(c)
                t.child[c] = n
                t = n
        return True

for _ in range(int(input())):
    n = int(input())
    tt = trie()
    flag = True
    for _ in range(n):
        tmp_s = list(map(int,input().rstrip()))
        if not flag:
            continue
        if not tt.push(tmp_s):
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")