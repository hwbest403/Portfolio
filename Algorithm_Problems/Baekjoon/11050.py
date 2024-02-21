if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    n, r = map(int,input().split())
    def fact(n) :
        result = 1
        for i in range(1, n+1) :
            result *= i
        return result
    print(int(fact(n)/(fact(r)*fact(n-r))))