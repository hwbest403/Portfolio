# coding = utf-8

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from collections import deque

    T = int(input())

    for _ in range(T) :
        n, m = map(int,input().split())
        folder = list(map(int,input().split()))
        printer = deque()
        for idx, file in enumerate(folder) :
            printer.append([idx, file])
        res = 1
        while True :
            tmp_file = printer.popleft()
            if tmp_file[1] == max(folder) :
                if tmp_file[0] == m :
                    print(res)
                    break
                else :
                    res += 1
                    folder.remove(tmp_file[1])
            else :
                printer.append(tmp_file)
