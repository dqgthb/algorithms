# Python Competitive Programming Template (updated 2022-08-05)
# Created by dqgthb

# from collections import deque
# from heapq import heappush, heappop

# from functools import cmp_to_key, reduce, partial
# from collections import Counter, defaultdict as dd
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br


def main() -> None:
    init()
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    grid = [[False for _ in range(100)] for _ in range(100)]
    for _ in range(4):
        a, b, c, d = map(lambda x: int(x)-1, input().split())

        for i in range(a, c):
            for j in range(b, d):
                grid[i][j] = True

    cnt = 0
    for i in range(100):
        for j in range(100):
            if grid[i][j]:
                cnt += 1
    print(cnt)

    # ######## INPUT AREA END ############

    # TEMPLATE ###############################


def init() -> None:
    global input
    from sys import stdin, argv
    input = stdin.readline  # by default

    if len(argv) == 1:
        from os import path
        if path.isfile("i"):
            stdin = open("i")
            input = stdin.readline

    elif len(argv) == 2:
        stdin = open(argv[1])
        input = stdin.readline


if __name__ == "__main__":
    main()
