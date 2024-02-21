# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    for i in range(1,n+1) :
        print(f"Case #{i}: ", end="")
        print(*input().split()[::-1])
