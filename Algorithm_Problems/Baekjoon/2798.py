if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    from itertools import combinations
    n, m = map(int,input().split())
    board = list(map(int,input().split()))
    result = list()
    for choice in combinations(board, 3) :
        if sum(choice) <= m :
            result.append(sum(choice))
    print(max(result))