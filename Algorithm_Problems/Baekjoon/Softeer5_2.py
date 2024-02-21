import sys
from collections import deque
input = sys.stdin.readline

# h 조직도 높이, k 말단에 대기하는 업무 수, r 업무 날짜 수
h, k, r = map(int,input().split())
# 높이에 따른 전체 노드 개수
node_cnt = 2**(h+1)-1
# 말단 직원 수
leaf_cnt = 2**h
# 조직도를 저장할 리스트
tree = list(deque() for _ in range(node_cnt))
# 말단 직원의 업무 입력받기
for i in range(leaf_cnt) :
    # 말단 직원의 idx는 끝부분부터 leaf_cnt 수만큼 존재
    idx = node_cnt-leaf_cnt+i
    tree[idx] = deque(map(int,input().split()))
# 말단 직원 이외 상사는 왼쪽 오른쪽 업무를 다른 날짜에 처리하므로 deque 두개 사용
for i in range(node_cnt-leaf_cnt) :
    tree[i] = list(deque() for _ in range(2))
# 답 저장
res = 0
# 날짜 마다 업무 처리 루프
for day in range(r) :
    # 말단 제외 상사 라인
    for i in range(node_cnt - leaf_cnt) :
        # 홀수 짝수 날짜 마다 다름
        if (day+1) % 2 == 0 :
            # 짝수 날은 오른쪽 부하직원이 올린 업무 진행
            if len(tree[i][1]) != 0 :
                # 부서장이면 답에 더하기
                if i == 0 :
                    res += tree[i][1].popleft()
                # 부서장 아니면 다시 위로 올리기
                else :
                    # parent node의 idx는 child node의 idx따라 다름
                    if i % 2 != 0 :
                        tree[i//2][0].append(tree[i][1].popleft())
                    else :
                        tree[i//2-1][1].append(tree[i][1].popleft())
        # 홀수 날도 짝수와 동일하게 진행
        else :
            if len(tree[i][0]) != 0 :
                if i == 0 :
                    res += tree[i][0].popleft()
                else :
                    if i%2 != 0 :
                        tree[i//2][0].append(tree[i][0].popleft())
                    else :
                        tree[i//2-1][1].append(tree[i][0].popleft())
    # 말단 직원 업무 진행
    for i in range(leaf_cnt) :
        # 말단 직원의 idx
        idx = node_cnt - leaf_cnt + i
        # 동일하게 parent node에 업무 올림
        if len(tree[idx]) != 0 :
            if idx % 2 != 0 :
                tree[idx//2][0].append(tree[idx].popleft())
            else :
                tree[idx//2-1][1].append(tree[idx].popleft())
print(res)