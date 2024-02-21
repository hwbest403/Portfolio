# coding = utf-8

if __name__ == '__main__':
    t = int(input())
    result = []
    for _ in range(t):
        u = [
            ['w', 'w', 'w'],
            ['w', 'w', 'w'],
            ['w', 'w', 'w']
        ]
        d = [
            ['y', 'y', 'y'],
            ['y', 'y', 'y'],
            ['y', 'y', 'y']
        ]
        f = [
            ['r', 'r', 'r'],
            ['r', 'r', 'r'],
            ['r', 'r', 'r']
        ]
        b = [
            ['o', 'o', 'o'],
            ['o', 'o', 'o'],
            ['o', 'o', 'o']
        ]
        l = [
            ['g', 'g', 'g'],
            ['g', 'g', 'g'],
            ['g', 'g', 'g']
        ]
        r = [
            ['b', 'b', 'b'],
            ['b', 'b', 'b'],
            ['b', 'b', 'b']
        ]
        n = int(input())
        ops = input().split()
        for op in ops:
            plane = op[0]
            direction = op[1]
            if plane == 'U':
                if direction == '+':
                    u = [[row[i] for row in reversed(u)] for i in range(3)]
                    '''
                    u = [
                        [u[2][0], u[1][0], u[0][0]],
                        [u[2][1], u[1][1], u[0][1]],
                        [u[2][2], u[2][2], u[0][2]]
                    ]
                    '''
                    tmp = f[0]
                    f[0] = r[0]
                    r[0] = b[0]
                    b[0] = l[0]
                    l[0] = tmp

                if direction == '-':
                    u = [[row[i] for row in u] for i in reversed(range(3))]
                    '''
                    u = [
                        [u[0][2] u [1][2] u[2][2]
                        [u[0][1] u[1][1] u[2][1]
                    ]
                    '''
                    tmp = f[0]
                    f[0] = l[0]
                    l[0] = b[0]
                    b[0] = r[0]
                    r[0] = tmp

            if plane == 'D':
                if direction == '+':
                    d = [[row[i] for row in reversed(d)] for i in range(3)]
                    tmp = f[2]
                    f[2] = l[2]
                    l[2] = b[2]
                    b[2] = r[2]
                    r[2] = tmp

                if direction == '-':
                    d = [[row[i] for row in d] for i in reversed(range(3))]
                    tmp = f[2]
                    f[2] = r[2]
                    r[2] = b[2]
                    b[2] = l[2]
                    l[2] = tmp

            if plane == 'L':
                if direction == '+':
                    l = [[row[i] for row in reversed(l)] for i in range(3)]
                    tmp = [u[0][0], u[1][0], u[2][0]]
                    for i in range(3):
                        u[i][0] = b[2 - i][2]
                    for i in range(3):
                        b[i][2] = d[2 - i][0]
                    for i in range(3):
                        d[i][0] = f[i][0]
                    for i in range(3):
                        f[i][0] = tmp[i]

                if direction == '-':
                    l = [[row[i] for row in l] for i in reversed(range(3))]
                    tmp = [u[0][0], u[1][0], u[2][0]]
                    tmp.reverse()
                    for i in range(3):
                        u[i][0] = f[i][0]
                    for i in range(3):
                        f[i][0] = d[i][0]
                    for i in range(3):
                        d[i][0] = b[2 - i][2]
                    for i in range(3):
                        b[i][2] = tmp[i]

            if plane == 'R':
                if direction == '+':
                    r = [[row[i] for row in reversed(r)] for i in range(3)]
                    tmp = [u[0][2], u[1][2], u[2][2]]
                    tmp.reverse()
                    for i in range(3):
                        u[i][2] = f[i][2]
                    for i in range(3):
                        f[i][2] = d[i][2]
                    for i in range(3):
                        d[i][2] = b[2 - i][0]
                    for i in range(3):
                        b[i][0] = tmp[i]
                if direction == '-':
                    r = [[row[i] for row in r] for i in reversed(range(3))]
                    tmp = [u[0][2], u[1][2], u[2][2]]
                    for i in range(3):
                        u[i][2] = b[2 - i][0]
                    for i in range(3):
                        b[i][0] = d[2 - i][2]
                    for i in range(3):
                        d[i][2] = f[i][2]
                    for i in range(3):
                        f[i][2] = tmp[i]

            if plane == 'F':
                if direction == '+':
                    f = [[row[i] for row in reversed(f)] for i in range(3)]
                    tmp = [u[2][0], u[2][1], u[2][2]]
                    for i in range(3):
                        u[2][2 - i] = l[i][2]
                    for i in range(3):
                        l[i][2] = d[0][i]
                    for i in range(3):
                        d[0][i] = r[2 - i][0]
                    for i in range(3):
                        r[i][0] = tmp[i]

                if direction == '-':
                    f = [[row[i] for row in f] for i in reversed(range(3))]
                    tmp = [u[2][0], u[2][1], u[2][2]]
                    tmp.reverse()
                    for i in range(3):
                        u[2][i] = r[i][0]
                    for i in range(3):
                        r[i][0] = d[0][2 - i]
                    for i in range(3):
                        d[0][i] = l[i][2]
                    for i in range(3):
                        l[i][2] = tmp
            if plane == 'B':
                if direction == '+':
                    new_b = [[row[i] for row in reversed(b)] for i in range(3)]
                    tmp = [u[0][0], u[0][1], u[0][2]]
                    tmp.reverse()
                    for i in range(3):
                        u[0][i] = r[i][2]
                    for i in range(3):
                        r[i][2] = d[2][2 - i]
                    for i in range(3):
                        d[2][i] = l[i][0]
                    for i in range(3):
                        l[i][0] = tmp[i]
                    b = new_b
                if direction == '-':
                    new_b = [[row[i] for row in b] for i in reversed(range(3))]
                    tmp = [u[0][0], u[0][1], u[0][2]]
                    for i in range(3):
                        u[0][i] = l[2 - i][0]
                    for i in range(3):
                        l[i][0] = d[2][i]
                    for i in range(3):
                        d[2][i] = r[2 - i][2]
                    for i in range(3):
                        r[i][2] = tmp[i]
                    b = new_b
        result.append(u)
    for res in result:
        for row in res:
            for comp in row:
                print(comp, end='')
            print()