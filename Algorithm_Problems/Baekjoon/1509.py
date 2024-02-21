# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    def getdata():
        board = list(input())
        return board

    board = getdata()
    board.pop()
    n = len(board)
    # dp 배열 생성
    dp = list(list(0 for _ in range(n)) for _ in range(n))
    # dp 배열 초기화 -> 이중배열 dp[i][j]는 i번째 문자부터 j번째 문자까지 펠린드롬인지
    # i부터 i까지, 즉 자기 자신은 스스로 펠린드롬 만족
    # if문은 본인과 바로 다음 문자 비교해서 같은 문자면 펠린드롬
    for i in range(n) :
        dp[i][i] = 1
        if i!=n-1 and board[i] == board[i+1] :
            dp[i][i+1] = 1
    # 이후 나머지 배열을 채우기 위한 과정
    # 다이나믹 프로그래밍 -> 점화식
    # i+1부터 j-1이 펠린드롬 & i와 j의 문자가 같으면 i부터 j도 펠린드롬임
    # 각 문자 자리에서 바로 다음 문자(2의 크기를 갖는)까지는 체크된 상태
    # 3의 크기를 갖는 부분 문자열 계산
    # jump를 2부터 n-1까지 -> left는 0부터 n-jump까지
    for jump in range(2,n) :
        for left in range(n-jump) :
            right = left + jump
            if board[left] == board[right] and dp[left+1][right-1] == 1:
                dp[left][right] = 1
    # 펠린드롬 분할의 최소값을 구하는 과정
    # 다이나믹 프로그래밍 -> 점화식
    # dp2[i] -> i번째까지의 펠린드롬 분할 최소값
    # dp2[0] -> 1 이것의 의미는 0번부터 0번까지 펠린드롬 분할은 1개라는 뜻
    # dp2[1] -> min(dp2[0]+1, dp[2]) 이것은 1번 문자 하나 자체로 펠린드롬이기 때문에 1번 문자 제외
    # 이전문자들에서 펠린드롬 분할 최소 + 1 이 최소가 될 수 있고, 또는 1번문자를 포함한 문자열에서 펠린드롬 분할 수가 최소가 될 수
    # 있다는 뜻
    # 결과적으로 dp[n] = min(dp[n-tmp]+1,dp[n]) 여기서 n-tmp 다음부터 n까지 펠린드롬 분할일 경우이고
    # 이 경우 n-tmp까지 최소 분할수 + 1 이나 전체의 최소 분할 수 중 작은 값을 선택
    dp2 = list(i+1 for i in range(n))
    for right in range(n) :
        for left in range(right,-1,-1) :
            if dp[left][right] == 1:
                if left == 0 :
                    dp2[right] = 1
                    continue
                dp2[right] = min(dp2[left-1]+1,dp2[right])
    print(dp2[n-1])