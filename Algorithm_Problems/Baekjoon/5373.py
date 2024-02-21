# coding = utf-8

if __name__ == '__main__':
    import sys
    import copy
    input = sys.stdin.readline

    T = int(input())

    def getdata():
        n = int(input())
        board = (list(input().split()))
        return n, board

    def spin(space, dir, U, D, F, B, L, R) :
        if space == 'U' :
            if dir == '+' :
                tmp = copy.deepcopy(F[0])
                F[0] = R[0]
                R[0] = B[0]
                B[0] = L[0]
                L[0] = tmp
                tmp1, tmp2 = copy.deepcopy(U[0][0]), copy.deepcopy(U[0][1])
                U[0][0], U[0][1] = U[2][0], U[1][0]
                U[2][0], U[1][0] = U[2][2], U[2][1]
                U[2][2], U[2][1] = U[0][2], U[1][2]
                U[0][2], U[1][2] = tmp1, tmp2
            if dir == '-' :
                tmp = copy.deepcopy(F[0])
                F[0] = L[0]
                L[0] = B[0]
                B[0] = R[0]
                R[0] = tmp
                tmp1, tmp2 = copy.deepcopy(U[0][0]), copy.deepcopy(U[0][1])
                U[0][0], U[0][1] = U[0][2], U[1][2]
                U[0][2], U[1][2] = U[2][2], U[2][1]
                U[2][2], U[2][1] = U[2][0], U[1][0]
                U[2][0], U[1][0] = tmp1, tmp2
        if space == 'D' :
            if dir == '+' :
                tmp = copy.deepcopy(F[2])
                F[2] = L[2]
                L[2] = B[2]
                B[2] = R[2]
                R[2] = tmp
                tmp1, tmp2 = copy.deepcopy(D[0][0]), copy.deepcopy(D[0][1])
                D[0][0], D[0][1] = D[0][2], D[1][2]
                D[0][2], D[1][2] = D[2][2], D[2][1]
                D[2][2], D[2][1] = D[2][0], D[1][0]
                D[2][0], D[1][0] = tmp1, tmp2
            if dir == '-' :
                tmp = copy.deepcopy(F[2])
                F[2] = R[2]
                R[2] = B[2]
                B[2] = L[2]
                L[2] = tmp
                tmp1, tmp2 = copy.deepcopy(D[0][0]), copy.deepcopy(D[0][1])
                D[0][0], D[0][1] = D[2][0], D[1][0]
                D[2][0], D[1][0] = D[2][2], D[2][1]
                D[2][2], D[2][1] = D[0][2], D[1][2]
                D[0][2], D[1][2] = tmp1, tmp2
        if space == 'F' :
            if dir == '+' :
                tmp = copy.deepcopy(U[2])
                for i in range(3) :
                    U[2][i] = L[-i-1][2]
                for i in range(3) :
                    L[i][2] = D[2][i]
                for i in range(3) :
                    D[2][i] = R[-i-1][0]
                for i in range(3):
                    R[i][0] = tmp[i]
                tmp1, tmp2 = copy.deepcopy(F[0][0]), copy.deepcopy(F[0][1])
                F[0][0], F[0][1] = F[2][0], F[1][0]
                F[2][0], F[1][0] = F[2][2], F[2][1]
                F[2][2], F[2][1] = F[0][2], F[1][2]
                F[0][2], F[1][2] = tmp1, tmp2
            if dir == '-' :
                tmp = copy.deepcopy(U[2])
                for i in range(3) :
                    U[2][i] = R[i][0]
                for i in range(3) :
                    R[i][0] = D[2][-i-1]
                for i in range(3) :
                    D[2][i] = L[i][2]
                for i in range(3):
                    L[i][2] = tmp[-i-1]
                tmp1, tmp2 = copy.deepcopy(F[0][0]), copy.deepcopy(F[0][1])
                F[0][0], F[0][1] = F[0][2], F[1][2]
                F[0][2], F[1][2] = F[2][2], F[2][1]
                F[2][2], F[2][1] = F[2][0], F[1][0]
                F[2][0], F[1][0] = tmp1, tmp2
        if space == 'B' :
            if dir == '+':
                tmp = copy.deepcopy(U[0])
                for i in range(3):
                    U[0][i] = R[i][2]
                for i in range(3):
                    R[i][2] = D[0][-i - 1]
                for i in range(3):
                    D[0][i] = L[i][0]
                for i in range(3):
                    L[i][0] = tmp[-i - 1]
                tmp1, tmp2 = copy.deepcopy(B[0][0]), copy.deepcopy(B[0][1])
                B[0][0], B[0][1] = B[2][0], B[1][0]
                B[2][0], B[1][0] = B[2][2], B[2][1]
                B[2][2], B[2][1] = B[0][2], B[1][2]
                B[0][2], B[1][2] = tmp1, tmp2
            if dir == '-':
                tmp = copy.deepcopy(U[0])
                for i in range(3):
                    U[0][i] = L[-i - 1][0]
                for i in range(3):
                    L[i][0] = D[0][i]
                for i in range(3):
                    D[0][i] = R[-i - 1][2]
                for i in range(3):
                    R[i][2] = tmp[i]
                tmp1, tmp2 = copy.deepcopy(B[0][0]), copy.deepcopy(B[0][1])
                B[0][0], B[0][1] = B[0][2], B[1][2]
                B[0][2], B[1][2] = B[2][2], B[2][1]
                B[2][2], B[2][1] = B[2][0], B[1][0]
                B[2][0], B[1][0] = tmp1, tmp2
        if space == 'L' :
            if dir == '+' :
                tmp = copy.deepcopy(list(zip(*U))[0])
                for i in range(3):
                    U[i][0] = B[-i-1][2]
                for i in range(3):
                    B[i][2] = D[i][0]
                for i in range(3):
                    D[i][0] = F[-i-1][0]
                for i in range(3):
                    F[i][0] = tmp[i]
                tmp1, tmp2 = copy.deepcopy(L[0][0]), copy.deepcopy(L[0][1])
                L[0][0], L[0][1] = L[2][0], L[1][0]
                L[2][0], L[1][0] = L[2][2], L[2][1]
                L[2][2], L[2][1] = L[0][2], L[1][2]
                L[0][2], L[1][2] = tmp1, tmp2
            if dir == '-' :
                tmp = copy.deepcopy(list(zip(*U))[0])
                for i in range(3):
                    U[i][0] = F[i][0]
                for i in range(3):
                    F[i][0] = D[-i-1][0]
                for i in range(3):
                    D[i][0] = B[i][2]
                for i in range(3):
                    B[i][2] = tmp[-i-1]
                tmp1, tmp2 = copy.deepcopy(L[0][0]), copy.deepcopy(L[0][1])
                L[0][0], L[0][1] = L[0][2], L[1][2]
                L[0][2], L[1][2] = L[2][2], L[2][1]
                L[2][2], L[2][1] = L[2][0], L[1][0]
                L[2][0], L[1][0] = tmp1, tmp2
        if space == 'R' :
            if dir == '+' :
                tmp = copy.deepcopy(list(zip(*U))[2])
                for i in range(3):
                    U[i][2] = F[i][2]
                for i in range(3):
                    F[i][2] = D[-i-1][2]
                for i in range(3):
                    D[i][2] = B[i][0]
                for i in range(3):
                    B[i][0] = tmp[-i-1]
                tmp1, tmp2 = copy.deepcopy(R[0][0]), copy.deepcopy(R[0][1])
                R[0][0], R[0][1] = R[2][0], R[1][0]
                R[2][0], R[1][0] = R[2][2], R[2][1]
                R[2][2], R[2][1] = R[0][2], R[1][2]
                R[0][2], R[1][2] = tmp1, tmp2
            if dir == '-' :
                tmp = copy.deepcopy(list(zip(*U))[2])
                for i in range(3):
                    U[i][2] = B[-i-1][0]
                for i in range(3):
                    B[i][0] = D[i][2]
                for i in range(3):
                    D[i][2] = F[-i-1][2]
                for i in range(3):
                    F[i][2] = tmp[i]
                tmp1, tmp2 = copy.deepcopy(R[0][0]), copy.deepcopy(R[0][1])
                R[0][0], R[0][1] = R[0][2], R[1][2]
                R[0][2], R[1][2] = R[2][2], R[2][1]
                R[2][2], R[2][1] = R[2][0], R[1][0]
                R[2][0], R[1][0] = tmp1, tmp2
        return

    def printans(U) :
        for i in range(3) :
            for j in range(3) :
                print(U[i][j], end="")
            print()
        return

    def printcount(a) :
        res = 0
        for i in range(3) :
            res += B[i].count(a)+F[i].count(a)+L[i].count(a)+R[i].count(a)+U[i].count(a)+D[i].count(a)
        return print(res)

    for _ in range(T) :
        U = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
        D = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
        F = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
        B = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
        L = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
        R = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
        n, board = getdata()
        for i in range(n) :
            # print(f"==={i}th===")
            spin(board[i][0], board[i][1], U, D, F, B, L, R)
            # printcount('w')
            # print("===U===")
            # for i in range(3) :
            #     print(U[i])
            # print("===D===")
            # for i in range(3):
            #     print(D[i])
            # print("===F===")
            # for i in range(3):
            #     print(F[i])
            # print("===R===")
            # for i in range(3):
            #     print(R[i])
            # print("===B===")
            # for i in range(3):
            #     print(B[i])
            # print("===L===")
            # for i in range(3):
            #     print(L[i])
        # print(U)
        # print(D)
        # print(F)
        # print(B)
        # print(R)
        # print(L)
        printans(U)

