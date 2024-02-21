import sys
input = sys.stdin.readline

# N 참가자 수
n = int(input())
# 매회 점수를 저장하기 위한 이중 배열 내부 배열 [점수, 몇번째 참가자]
score = list(list([0, 0] for _ in range(n)) for _ in range(4))
for i in range(3) :
    # i번째 경기 점수 입력
    tmp_score = list(map(int,input().split()))
    for idx, num in enumerate(tmp_score) :
        # 몇번째 몇점인지 각각 저장
        tmp_score[idx] = [num, idx]
        # 마지막에 경기 총합계 나타내기 위한 각 경기 점수 합산
        score[3][idx][0] += num
        score[3][idx][1] = idx
    # 점수 높은 순 정렬
    tmp_score.sort(key=lambda x:x[0], reverse=True)
    score[i] = tmp_score
# 합산 점수 또한 정렬
score[3].sort(key=lambda x:x[0], reverse=True)

# 등수를 저장할 ans 리스트
ans = list(list(0 for _ in range(n)) for _ in range(4))
# score에는 매 경기 점수와 몇번째 참가자인지 들어있음
for idx1, competition in enumerate(score) :
    res = 1
    for idx2, s in enumerate(competition) :
        # 맨 앞은 1등
        if idx2 == 0:
            ans[idx1][s[1]] = res
        else :
            res += 1
            # 같은 점수는 높은 등수에 공동 순위
            if s[0] == competition[idx2-1][0] :
                ans[idx1][s[1]] = ans[idx1][competition[idx2-1][1]]
            else :
                ans[idx1][s[1]] = res

for i in ans :
    print(*i)