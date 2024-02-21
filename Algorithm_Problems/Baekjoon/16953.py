import sys

input = sys.stdin.readline

# dp[i] -> A를 i로 바꾸는데 필요한 최솟값
# if i의 1의자리수가 1이면 dp[i] = dp[i//10]+1
# if i가 짝수 dp[i] = dp[i//2]+1
# 1의자리수가 1이 아닌 홀수 => dp[i] = -1

a, b = map(int, input().split())
answer = float('inf')
def sol(a, b, cnt):
    global answer
    if a > b:
        return float('inf')
    if a == b:
        if cnt < answer:
            answer = cnt
        return cnt
    else:
        sol(a*10+1, b, cnt+1)
        sol(a*2, b, cnt+1)

sol(a, b, 0)
if answer == float('inf'):
    print(-1)
    exit()
print(answer+1)