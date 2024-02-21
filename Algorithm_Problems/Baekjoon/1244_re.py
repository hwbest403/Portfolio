# 아이디어

# 규칙
# 남학생 : 받은 수의 배수는 모두 스위치 상태 바꿈
# 여학생 : 1) 좌우 대칭 O -> 최대 좌우대칭 범위까지 모두 스위치 상태 바꿈
#       2) 좌우 대칭 X -> 받은 스위치 번호만 상태 바꿈

from ast import If
from re import S
import sys

input = sys.stdin.readline

sw_nm = int(input())
switch = list(map(int, input().split()))
st_num = int(input())
st_list = []

for _ in range(st_num):
    gender, number = list(map(int, input().split()))
    if gender == 1:
        st_list.append([gender, number, [x for x in range(1, sw_nm + 1) if x % number == 0]])
    else:
        st_list.append([gender, number])


def change_switch(x, loc: list):
    if x[loc] == 0:
        x[loc] = 1
    elif x[loc] == 1:
        x[loc] = 0
    return x


def find_symmetric_range(x, start_loc):
    iter = 1
    while (0 <= start_loc + iter < (sw_nm - 1)) and (0 <= start_loc - iter < (sw_nm - 1)):
        left = start_loc - iter
        right = start_loc + iter
        if x[left] == x[right]:
            iter += 1
        else:
            break
    return iter - 1


for idx, student in enumerate(st_list):
    print('student', student)

    # 남학생인 경우
    if student[0] == 1:
        for i in student[-1]:
            switch = change_switch(switch, i - 1)
    # 여학생인 경우
    else:
        tmp = find_symmetric_range(switch, student[1] - 1)

        print('tmp', tmp)
        if tmp > 0:
            switch = change_switch(switch, student[1] - 1)
            for j in range(1, tmp + 1):
                switch = change_switch(switch, student[1] - 1 + j)
                switch = change_switch(switch, student[1] - 1 - j)
        else:
            switch = change_switch(switch, student[1] - 1)

    print('switch', switch)
# print('switch',switch)
flag = 0
for s in switch:
    print(s, end=' ')
    flag += 1
    if flag % 20 == 0:
        print()

