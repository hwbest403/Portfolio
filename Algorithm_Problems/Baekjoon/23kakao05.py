import math
from itertools import combinations

def solution(n, tops):
    answer = 0
    # n
    # n+1
    # 1*(2n+1), 2*0 => (2n+2)H0
    # 1*(2n+1-2k), 2*k => (2n+2-2k)Hk or (k+1)H(2n+1-2k)
    # 1*1, 2*n => (n+1)H1
    ls = list()
    for i in range(n):
        if tops[i] == 1:
            ls.append(i)
    def nums(n):
        tmp = 0
        for i in range(n+1):
            if 2*n+1-2*i > i:
                tmp += math.comb(2*n+2-2*i+i-1, i)%10007
                tmp %= 10007
            else:
                tmp += math.comb(i+1+2*n+1-2*i-1, 2*n+1-2*i)%10007
                tmp %= 10007
        return tmp
    for i in range(len(ls)+1):
        for choice in combinations(ls, i):
            print(choice)
            if not choice:
                answer += nums(n)
                print(answer)
                continue
            tp = 1
            for idx in range(len(choice)):
                if idx == 0:
                    tp *= nums(choice[idx]-0)
                else:
                    tp *= nums(choice[idx]-choice[idx-1]-1)
            tp *= nums(n-choice[len(choice)-1]-1)
            answer += tp
    return answer

print(solution(2, [1, 1]))