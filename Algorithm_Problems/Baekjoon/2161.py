# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque

    n = int(input())
    num_list = deque(i for i in range(1, n+1))
    while True :
        print(num_list.popleft(), end=" ")
        if not num_list :
            break
        num_list.append(num_list.popleft())