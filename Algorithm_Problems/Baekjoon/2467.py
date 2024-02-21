# coding = utf-8

import sys
input = sys.stdin.readline

def twopointer(ls, n) :
    res = 3*(10**9)
    left, right = 0, n-1
    res_left, res_right = left, right
    while left < right :
        # print(left, right)
        tmp = ls[left] + ls[right]
        if abs(tmp) < abs(res) :
            res = abs(tmp)
            res_left, res_right = left, right
        if tmp < 0 :
            left += 1
        elif tmp > 0 :
            right -= 1
        else :
            return ls[res_left], ls[res_right]
    return ls[res_left], ls[res_right]

n = int(input())
num_list = list(map(int,input().split()))
print(*twopointer(num_list, n))