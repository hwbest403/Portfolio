# coding = utf-8

import sys
input = sys.stdin.readline

def binarysearch(ls, num):
    left = 0
    right = len(ls)-1
    while left <= right:
        mid = (left+right) // 2
        if ls[mid] == num:
            return 1
        elif ls[mid] < num:
            left = mid + 1
        else :
            right = mid - 1
    return 0

n = int(input())
num_list = list(map(int,input().split()))
num_list.sort()
print(num_list)
m = int(input())
call = list(map(int, input().split()))
for num in call:
    print(binarysearch(num_list, num), end=" ")