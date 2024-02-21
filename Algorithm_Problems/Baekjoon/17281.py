# coding = utf-8

import sys
input = sys.stdin.readline
from itertools import permutations
from collections import deque

n = int(input())
board = list(list(map(int, input().split())) for _ in range(n))

answer = 0
for choice in permutations([1, 2, 3, 4, 5, 6, 7, 8], 8):
    tmp_score = 0
    batter = deque(choice)
    batter.insert(3, 0)
    for inning in board:
        base = deque(False for _ in range(3))
        Run = 0
        Out = 0
        while True:
            if inning[batter[0]] == 0:
                Out += 1
            elif inning[batter[0]] == 1:
                if base[-1] == True:
                    Run += 1
                base.pop()
                base.appendleft(True)
            elif inning[batter[0]] == 2:
                for idx in range(2):
                    if base[-1] == True:
                        Run += 1
                    base.pop()
                    if idx == 0:
                        base.appendleft(True)
                    else:
                        base.appendleft(False)
            elif inning[batter[0]] == 3:
                for idx in range(3):
                    if base[-1] == True:
                        Run += 1
                    base.pop()
                    if idx == 0:
                        base.appendleft(True)
                    else:
                        base.appendleft(False)
            elif inning[batter[0]] == 4:
                Run += base.count(True)
                Run += 1
                base = deque(False for _ in range(3))
            batter.rotate(-1)
            if Out == 3:
                break
        tmp_score += Run
    answer = max(answer, tmp_score)
print(answer)