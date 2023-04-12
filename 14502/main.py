# Python Competitive Programming Template (updated 2022-08-05)
# Created by dqgthb

# from collections import deque
# from heapq import heappush, heappop

# from functools import cmp_to_key, reduce, partial
# from collections import Counter, defaultdict as dd
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br

from typing import Tuple, TypeVar
from typing import Callable, List


input: Callable[[], str]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n: int
m: int
virusSources: List[Tuple[int, int]]
safeArea: int


def main() -> None:
    init()
    global n, m, virusSources

    n, m = map(int, input().split())
    mat = [[int(i) for i in input().split()] for _ in range(n)]

    virusSources = []
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                virusSources.append((i, j))

    global safeArea
    safeArea = 0

    wall(0, mat, 0, 0)
    

    print(safeArea)


def virus(mat: List[List[int]]) -> int:
    for i, j in virusSources:
        dfs(mat, i, j)
    # parr(mat)
    # print()
    return countSafe(mat)


def countSafe(mat: List[List[int]]) -> int:
    count = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                count += 1
    return count


def dfs(mat: List[List[int]], y: int, x: int) -> None:
    mat[y][x] = 2

    for i, j in zip(dx, dy):
        ni = y + i
        nj = x + j
        if 0 <= ni < n and 0 <= nj < m:
            if mat[ni][nj] == 0:
                dfs(mat, ni, nj)


def wall(wallCount: int, mat: List[List[int]], i: int, j: int) -> None:
    global safeArea
    while i < n:
        while j < m:
            if mat[i][j] == 0:
                mat[i][j] = 8
                if wallCount < 2:
                    wall(wallCount + 1, mat, i, j)
                else:
                    cpy = [i[:] for i in mat]
                    safeArea = max(virus(cpy), safeArea)
                mat[i][j] = 0
            j += 1
            if j == m:
                j = 0
                break
        i += 1


# TEMPLATE ###############################


StrOrInt = TypeVar('StrOrInt', str, int)


def parr(arr: List[List[StrOrInt]]) -> None:
    for e in arr:
        print(e)


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
