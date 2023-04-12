# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from sys import stdin, argv
from os import path

# from collections import deque
# from heapq import heappush, heappop
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br


def main() -> None:
    # sys.setrecursionlimit(10**9)

    N = int(input())

    grid = [[False for _ in range(100)] for _ in range(100)]

    for _ in range(N):
        a, b = map(int, input().split())

        for i in range(10):
            for j in range(10):
                grid[a+i][b+j] = True

    cnt = 0
    for i in range(100):
        for j in range(100):
            if grid[i][j]:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
