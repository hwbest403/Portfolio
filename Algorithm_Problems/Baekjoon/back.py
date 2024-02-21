import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
k = int(input())

def mergeSort(ls) :

    if len(ls) <= 1 :
        return ls

    mid = len(ls) // 2
    # Divide
    left_ls = mergeSort(ls[:mid])
    right_ls = mergeSort(ls[mid:])
    # Conquer&Combine
    merge_ls = merge(left_ls, right_ls)
    return merge_ls

#Conquer
def merge(ls1, ls2):
    merge_ls = list()
    print(ls1, ls2)
    while len(ls1) > 0 and len(ls2) > 0:
        if ls1[0] <= ls2[0]:
            merge_ls.append(ls1.pop(0))
        else:
            merge_ls.append(ls2.pop(0))
    if len(ls1) > 0:
        merge_ls += ls1
    if len(ls2) > 0:
        merge_ls += ls2
    print(merge_ls)
    return merge_ls

mergeSort(num_list)