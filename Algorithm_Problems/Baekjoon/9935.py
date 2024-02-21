# coding = utf-8

import sys
input = sys.stdin.readline

str1 = input().rstrip()
explosive = list(input().rstrip())

stack = list()
for c in str1:
    stack.append(c)
    if len(stack) >= len(explosive):
        if stack[-len(explosive):] == explosive:
            for _ in range(len(explosive)):
                stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")