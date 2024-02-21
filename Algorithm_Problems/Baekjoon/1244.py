# coding = utf-8

import sys
input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))
m = int(input())

def changeswitch(idx):
    if switch[idx] == 0:
        switch[idx] = 1
    else:
        switch[idx] = 0

def boy(number):
    idx = number-1
    while idx<n:
        changeswitch(idx)
        idx += number

def girl(number):
    idx = number-1
    changeswitch(idx)
    l, r = idx-1, idx+1
    while l>=0 and r<n and switch[l] == switch[r]:
        changeswitch(l)
        changeswitch(r)
        l -= 1
        r += 1

def sol(gender, number):
    if gender == 1:
        boy(number)
    else:
        girl(number)

def printswitch():
    idx = 0
    for number in switch:
        print(number, end=" ")
        idx += 1
        if idx % 20 == 0:
            print()

for _ in range(m) :
    g, num = map(int, input().split())
    sol(g, num)

printswitch()