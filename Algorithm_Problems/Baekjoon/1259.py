# coding = utf-8

import sys
input = sys.stdin.readline

while True :
    s = input().rstrip()
    if s == str(0) :
        break
    l, r = 0, len(s)-1
    flag = True
    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            print("no")
            flag = False
            break
    if flag:
        print("yes")