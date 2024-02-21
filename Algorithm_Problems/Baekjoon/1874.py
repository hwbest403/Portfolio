# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque

    n = int(input())
    ls, ans, stack = list(), list(), deque()
    ls2 = deque(i+1 for i in range(n+1))
    # stack -> stack
    # stack <- push 방향
    # stack -> pop 방향
    for _ in range(n) :
        ls.append(int(input()))
    num = 1
    stack.append(0)
    for i in ls :
        if stack[-1] < i :
            while stack[-1] != i :
                stack.append(ls2.popleft())
                ans.append('+')
            stack.pop()
            ans.append('-')
        elif stack[-1] == i :
            stack.pop()
            ans.append('-')
        else :
            print("NO")
            sys.exit()
    for i in ans :
        print(i)