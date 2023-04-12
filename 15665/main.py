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
    pass

    global N, M

    N, M = map(int, input().split())
    global ARR
    ARR = [int(i) for i in input().split()]
    ARR = list(set(ARR))
    ARR.sort()
    N = len(ARR)

    cand = []
    dfs(0, 0, cand)


def dfs(num, idx, cand):

    if num == M:
        print(*cand)
        return

    for i in range(N):
        cand.append(ARR[i])
        dfs(num + 1, 0, cand)
        cand.pop()


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
