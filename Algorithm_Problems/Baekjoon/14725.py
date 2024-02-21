# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    def getdata():
        n = int(input())
        board = list(list(input().rstrip()[1:].split()) for _ in range(n))
        return n, board

    n, board = getdata()
    food = dict()
    for item in board :
        tmp = food
        for f in item :
            if f not in tmp :
                tmp[f] = dict()
            tmp = tmp[f]
    print(food)
    def printresult(food, i) :
        tmp_key = sorted(food.keys())
        for k in tmp_key :
            print("--"*i + k)
            printresult(food[k],i+1)

    printresult(food,0)