def solution(coin, cards):
    answer = 0
    n = len(cards)
    hand_set = set()
    hand = list(False for _ in range(n+1))
    need_visited = list(False for _ in range(n+1))
    can_go = 1
    idx = 0
    while idx <= n:
        print(idx, coin, can_go, answer)
        if idx <= n//3-1:
            hand[cards[idx]] = True
            hand_set.add(cards[idx])
            if hand[n+1-cards[idx]] == True:
                hand[cards[idx]] = False
                hand[n+1-cards[idx]] = False
                hand_set.remove(cards[idx])
                hand_set.remove(n+1-cards[idx])
                can_go += 1
            idx += 1
        else:
            if can_go == 0:
                for i in hand_set:
                    if need_visited[n+1-i] and coin >= 1:
                        hand[i] = False
                        hand_set.remove(i)
                        need_visited[n+1-i] = False
                        can_go += 1
                        coin -= 1
                        break
                if can_go == 0:
                    for i in range(1, n//2+1):
                        if need_visited[i] and need_visited[n+1-i] and coin >= 2:
                            need_visited[i] = False
                            need_visited[n+1-i] = False
                            coin -= 2
                            can_go += 1
                if can_go == 0:
                    break
            if can_go >= 1:
                can_go -= 1
                answer += 1
                if idx != n:
                    need_visited[cards[idx]] = True
                    need_visited[cards[idx+1]] = True
                idx += 2
    return answer

print(solution(2, [1,5,3,4,2,6]))