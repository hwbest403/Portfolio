import sys

input = sys.stdin.readline

while True:
    a, b, c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if b + c <= a or a + c <= b or a + b <= c:
        print("Invalid")
    elif a == b and b == c:
        print("Equilateral")
    elif a != b and b != c and a != c:
        print("Scalene")
    elif (a == b and b != c) or (a == c and b != c) or (b == c and a != b):
        print("Isosceles")