# Python Competitive Programming Template (updated 2022-08-05)
# Created by dqgthb

# from collections import deque
# from heapq import heappush, heappop

# from functools import cmp_to_key, reduce, partial
# from collections import Counter, defaultdict as dd
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br


from typing import Callable, List, Optional, TypeVar
input: Callable[[], str]
n: int
map_: List[List[int]]
dp: List[List[Optional[int]]]


def main() -> None:
    init()
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global n, map_, dp

    n = int(input())
    map_ = [[int(i) for i in input().split()] for _ in range(n)]

    # ######## INPUT AREA END ############

    ans = solution(n, map_)
    print(ans)


def solution(n: int, map_: List[List[int]]) -> int:
    global dp
    dp = [[None for _ in range(n)] for _ in range(n)]

    return DP(0, 0)


def DP(i: int, j: int) -> int:
    if i == j == n-1:
        return 1

    val = dp[i][j]
    if val is not None:
        return val

    jump: int = map_[i][j]

    if jump == 0:
        return 0

    paths: int = 0
    if i + jump < n:
        paths += DP(i + jump, j)

    if j + jump < n:
        paths += DP(i, j + jump)

    dp[i][j] = paths
    return paths


# TEMPLATE ###############################
T = TypeVar("T", str, int)


def parr(arr: List[List[T]]) -> None:
    print('\n'.join(str(i) for i in arr))


def Mat(h: int, w: int, default: None | str | int = None) -> \
        List[List[None | str | int]]:
    return [[default for _ in range(w)] for _ in range(h)]


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
