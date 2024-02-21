from collections import defaultdict

def printboard(board):
    for row in board:
        print(row)

def solution(friends, gifts):
    answer = list(0 for _ in range(len(friends)))
    nmap = defaultdict(int)
    gift_info = list(list(0 for _ in range(len(friends))) for _ in range(len(friends)))
    gift_idx = list(0 for _ in range(len(friends)))
    for idx, f in enumerate(friends):
        nmap[f] = idx
    for g in gifts:
        tmp = list(g.split())
        gift_info[nmap[tmp[0]]][nmap[tmp[1]]] += 1
    for i in range(len(friends)):
        give = sum(gift_info[i])
        take = 0
        for j in range(len(friends)):
            take += gift_info[j][i]
        gift_idx[i] = give-take
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if gift_info[i][j] > gift_info[j][i]:
                answer[i] += 1
            elif gift_info[i][j] < gift_info[j][i]:
                answer[j] += 1
            else:
                if gift_idx[i] > gift_idx[j]:
                    answer[i] += 1
                elif gift_idx[i] < gift_idx[j]:
                    answer[j] += 1
                else:
                    pass
    return max(answer)