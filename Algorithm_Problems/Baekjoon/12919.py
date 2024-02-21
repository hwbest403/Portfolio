import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()
res = 0

def sol(S, T, flag):
    global res
    print(S)
    if len(S) < len(T):
        if flag:
            sol('A'+S, T, False)
            sol(S+'B', T, True)
        else:
            sol(S+'A', T, False)
            sol('B'+S, T, True)
    else:
        if flag:
            if S == T:
                res = 1
                return
        else:
            if S[::-1] == T:
                res = 1
                return

sol(S, T, False)
print(res)