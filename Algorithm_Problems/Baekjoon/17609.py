# coding = utf-8

import sys
input = sys.stdin.readline

def sol(s):
    l, r = 0, len(s)-1
    flag = False
    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] != s[r] and not flag:
            if s[l+1] == s[r] and s[l] == s[r-1]:
                l1, r1 = l+1, r
                l2, r2 = l, r-1
                flag1, flag2 = True, True
                while l1 <= r1:
                    if s[l1] == s[r1]:
                        l1 += 1
                        r1 -= 1
                    else:
                        flag1 = False
                        break
                while l2 <= r2:
                    if s[l2] == s[r2]:
                        l2 += 1
                        r2 -= 1
                    else:
                        flag2 = False
                        break
                if flag1 or flag2:
                    return 1
                return 2
            elif s[l+1] == s[r]:
                l += 1
                flag = True
            elif s[l] == s[r-1]:
                r -= 1
                flag = True
            else:
                return 2
        elif s[l] != s[r] and flag:
            return 2
    if flag:
        return 1
    return 0

for _ in range(int(input())):
    s = input().rstrip()
    print(sol(s))