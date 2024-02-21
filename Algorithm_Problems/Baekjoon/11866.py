# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque

    n, k = map(int, input().split())
    num_list = deque(i for i in range(1, n+1))
    result = list()
    print('<',end="")
    while len(num_list) != 1 :
        for _ in range(k-1) :
            num_list.append(num_list.popleft())
        print(num_list.popleft(), end=", ")
    print(num_list.popleft(), end=">")