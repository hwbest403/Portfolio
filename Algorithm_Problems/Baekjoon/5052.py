# coding = utf-8

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    trie = dict()
    flag = True
    for _ in range(n):
        tmp_s = input().rstrip()
        if not flag:
            continue
        tmp_trie = trie
        for idx, c in enumerate(tmp_s):
            if idx == len(tmp_s)-1 and c in tmp_trie:
                flag = False
                break
            if c in tmp_trie:
                tmp_trie = tmp_trie[c]
                if len(tmp_trie) == 0:
                    flag = False
                    break
            else:
                tmp_trie[c] = dict()
                tmp_trie = tmp_trie[c]

    if flag:
        print("YES")
    else:
        print("NO")