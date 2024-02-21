# coding = utf-8

if __name__ == '__main__':
    import sys
    from fractions import Fraction
    input = sys.stdin.readline

    def getdata():
        n, m = map(int,input().split())
        return n, m

    def fact(a) :
        res = 1
        for i in range(1, a+1) :
            res *= i
        return res

    n, m = getdata()

    print(Fraction(fact(n),(fact(m)*fact(n-m))))