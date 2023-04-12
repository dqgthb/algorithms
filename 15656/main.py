# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from sys import stdin, argv
from os import path

# from collections import deque
# from heapq import heappush, heappop
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br

ansSet = set()


def solve(arr, m):

    combinations = []

    dfs(arr, 0, 0, combinations)


def dfs(arr, num, idx, comb):
    if num == M:
        ansSet.add(tuple(comb))
        return

    for i in range(idx, len(arr)):
        comb.append(arr[i])
        dfs(arr, num + 1, i + 1, comb)
        comb.pop()


def main() -> None:
    # sys.setrecursionlimit(10**9)

    global N, M
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    solve(arr, M)

    for e in ansSet:
        print(*e)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
