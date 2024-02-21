# coding = utf-8

import sys
input = sys.stdin.readline

n = int(input())
num_list = list(int(input()) for _ in range(n))
# stack -> num_list의 각 값과 pair를 이룰 수 있는 후보
stack = list()

res = 0
for num in num_list :
    while stack and stack[-1][0] < num :
        # 현재 들어오는 사람보다 작기 때문에 다음 사람은 작은 사람을 볼 수 없음
        stack.pop()
        # pair를 이룸
        res += 1
    # 현재 들어올 사람과 이미 있던 사람 pair
    if not stack :
        stack.append([num, 1])
        continue
    if len(stack)>0 :
        # 키가 같은 사람은 같은 사람과 하나 더 큰 사람까지 가능
        if num == stack[-1][0] :
            res += stack[-1][1]
            if stack[-1][1] != len(stack) :
                res += 1
            stack.append([num, stack[-1][1]+1])
        # 내림차순이기에 키가 작은사람은 이미 있던 사람 중 제일 끝 사람과만 pair 가능
        else :
            stack.append([num, 1])
            res += 1
print(res)