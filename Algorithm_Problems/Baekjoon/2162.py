if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    board = list(list(map(int,input().split())) for _ in range(n))

    def crosscheck(line1:list, line2:list)->bool :
        slope1 = (line1[3]-line1[1])/(line1[2]-line1[0])
        slope2 = (line2[3] - line2[1]) / (line2[2] - line2[0])
        if slope1 == slope2 :
            return False
        else :
            return True