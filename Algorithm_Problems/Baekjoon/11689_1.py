# coding = utf-8

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    n = int(input())
    result = n
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result *= 1 - (1 / i)
    if n > 1:
        result *= 1 - (1 / n)
    print(round(result))
