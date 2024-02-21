# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    # U R D L
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    def printboard(board, n) :
        for i in range(n) :
            print(board[i])

    def getdata():
        n, m = map(int,input().split())
        board = list(list(input().rstrip()) for _ in range(n))
        command = list(map(str,input().rstrip()))
        for idx, dir in enumerate(command) :
            if dir == 'U' :
                command[idx] = 0
            elif dir == 'R' :
                command[idx] = 1
            elif dir == 'D' :
                command[idx] = 2
            else :
                command[idx] = 3
        k, l = 0, 0
        for i in range(n) :
            for j in range(m) :
                if board[i][j] == '&' or board[i][j] == 'M' :
                    k += 1
                if board[i][j] == 'B' :
                    l += 1
                if board[i][j] == '@' :
                    ix, iy = i, j
        monster, box = dict(), dict()
        for i in range(k) :
            tmp=list(input().split())
            monster[int(tmp[0])-1,int(tmp[1])-1] = [int(tmp[3]), int(tmp[4]), int(tmp[5]), int(tmp[6]), tmp[2]]
        for i in range(l) :
            tmp = list(input().split())
            box[int(tmp[0])-1, int(tmp[1])-1] = [tmp[2], tmp[3]]
        return n, m, k, l, board, command, monster, box, ix, iy

    n, m, k, l, board, command, monster, box, ix, iy = getdata()
    # print(n, m, k, l)
    # printboard(board, n)
    # print(command)
    # print(monster)
    # print(box)

    def move(board, x, y, dir) :
        nx = x+dx[dir]
        ny = y+dy[dir]
        if 0<=nx<n and 0<=ny<m and board[nx][ny] != '#' :
            return nx, ny
        else :
            return x, y

    # LV, HP, ATT, DEF, EXP
    player = [1, 20, 2, 2, 0]
    max_hp = 20
    max_exp = 5
    # weapon, armor, accessories*4
    equipment = [0, 0, 0, 0, 0, 0]

    def printplayer(board, player, equipment, turn, max_hp, max_exp) :
        for i in range(n) :
            for j in range(m) :
                print(board[i][j], end="")
            print()
        print(f"Passed Turns : {turn}")
        print(f"LV : {player[0]}")
        print(f"HP : {player[1]}/{max_hp}")
        print(f"ATT : {player[2]}+{equipment[0]}")
        print(f"DEF : {player[3]}+{equipment[1]}")
        print(f"EXP : {player[4]}/{max_exp}")

    def sol(max_hp, max_exp) :
        turn = 0
        sx, sy = ix, iy
        board[ix][iy] = '.'
        for dir in command :
            sx, sy = move(board, sx, sy, dir)
            turn += 1
            if board[sx][sy] == '^' :
                if 'DX' in equipment :
                    player[1] -= 1
                else :
                    player[1] -= 5
                if player[1] <= 0 :
                    if 'RE' not in equipment :
                        player[1] = 0
                        printplayer(board, player, equipment, turn, max_hp, max_exp)
                        print("YOU HAVE BEEN KILLED BY SPIKE TRAP..")
                        return
                    else :
                        sx, sy = ix, iy
                        player[1] = max_hp
                        equipment.remove('RE')
            if board[sx][sy] == '&' :
                tmp = monster[(sx, sy)]
                m_hp = tmp[2]
                flag = 0
                if 'CO' in equipment :
                    flag = 1
                while True :
                    if flag == 0 :
                        tmp[2] -= max(1, player[2]+equipment[0]-tmp[1])
                    if flag == 1 :
                        if 'DX' not in equipment :
                            tmp[2] -= max(1, (player[2]+equipment[0])*2-tmp[1])
                        else :
                            tmp[2] -= max(1, (player[2] + equipment[0]) * 3 - tmp[1])
                        flag = 0
                    if tmp[2] <= 0 :
                        board[sx][sy] = '.'
                        if 'EX' in equipment :
                            player[4] += int(tmp[3]*(1.2))
                        else :
                            player[4] += int(tmp[3])
                        if player[4] >= max_exp :
                            player[4] = 0
                            player[0] += 1
                            max_hp += 5
                            player[1] = max_hp
                            player[2] += 2
                            player[3] += 2
                            max_exp += 5
                        if 'HR' in equipment :
                            player[1] += 3
                            if player[1] >= max_hp :
                                player[1] = max_hp
                        break
                    player[1] -= max(1, tmp[0]-player[3]-equipment[1])
                    if player[1] <= 0 :
                        if 'RE' not in equipment :
                            player[1] = 0
                            printplayer(board, player, equipment, turn, max_hp, max_exp)
                            print(f"YOU HAVE BEEN KILLED BY {tmp[4]}..")
                            return
                        else :
                            sx, sy = ix, iy
                            player[1] = max_hp
                            equipment.remove('RE')
                            tmp[2] = m_hp
                            break
            if board[sx][sy] == 'B':
                tmp = box[sx, sy]
                if tmp[0] == 'W' :
                    equipment[0] = int(tmp[1])
                elif tmp[0] == 'A' :
                    equipment[1] = int(tmp[1])
                else :
                    if tmp[1] not in equipment :
                        for i in range(2, 6) :
                            if equipment[i] == 0:
                                equipment[i] = tmp[1]
                                break
                board[sx][sy] = '.'
            if board[sx][sy] == 'M' :
                Hflag = 0
                if 'HU' in equipment :
                    player[1] = max_hp
                    Hflag = 1
                tmp = monster[sx, sy]
                m_hp = tmp[2]
                flag = 0
                if 'CO' in equipment:
                    flag = 1
                while True:
                    if flag == 0:
                        tmp[2] -= max(1, player[2] + equipment[0] - tmp[1])
                    if flag == 1:
                        if 'DX' not in equipment:
                            tmp[2] -= max(1, (player[2] + equipment[0]) * 2 - tmp[1])
                        else:
                            tmp[2] -= max(1, (player[2] + equipment[0]) * 3 - tmp[1])
                        flag = 0
                    if tmp[2] <= 0:
                        if 'EX' in equipment:
                            player[4] += int(tmp[3] * (1.2))
                        else:
                            player[4] += int(tmp[3])
                        if player[4] >= max_exp:
                            player[4] = 0
                            player[0] += 1
                            max_hp += 5
                            player[1] = max_hp
                            player[2] += 2
                            player[3] += 2
                            max_exp += 5
                        if 'HR' in equipment:
                            player[1] += 3
                            if player[1] >= max_hp:
                                player[1] = max_hp
                        board[sx][sy] = '@'
                        printplayer(board, player, equipment, turn, max_hp, max_exp)
                        print("YOU WIN!")
                        return
                    if Hflag == 0 :
                        player[1] -= max(1, tmp[0] - player[3] - equipment[1])
                    else :
                        Hflag = 0
                    if player[1] <= 0:
                        if 'RE' not in equipment:
                            player[1] = 0
                            printplayer(board, player, equipment, turn, max_hp, max_exp)
                            print(f"YOU HAVE BEEN KILLED BY {tmp[4]}..")
                            return
                        else:
                            sx, sy = ix, iy
                            player[1] = max_hp
                            equipment.remove('RE')
                            tmp[2] = m_hp
                            break
            # print(f"==={turn}th===")
            # board[ix][iy]='.'
            # dd = board[sx][sy]
            # board[sx][sy] = '@'
            # printboard(board,n)
            # print(f"===player===")
            # print(player)
            # print(f"===equipment===")
            # print(equipment)
            # board[sx][sy] = dd
        board[sx][sy] = '@'
        printplayer(board,player,equipment,turn,max_hp,max_exp)
        print("Press any key to continue.")

    sol(max_hp, max_exp)