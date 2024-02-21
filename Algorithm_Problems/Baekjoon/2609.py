if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def GCD(x, y) :
        while y :
            x, y = y, x%y
        return x

    def LCM(x, y) :
        return (x*y)//GCD(x,y)

    x, y = map(int,input().split())
    print(GCD(x,y))
    print(LCM(x,y))