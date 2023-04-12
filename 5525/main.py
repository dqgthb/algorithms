# Python Competitive Programming Template (updated 2022-08-05)
# Created by dqgthb

# from collections import deque
# from heapq import heappush, heappop

# from functools import cmp_to_key, reduce, partial
# from collections import Counter, defaultdict as dd
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br


from typing import Callable, List, Union
input: Callable[[], str]


def main() -> None:
    init()
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    N = int(input())
    M = int(input())
    S = input().strip()

    # ######## INPUT AREA END ############

    total = 0
    prev = S[0]
    IOIcnt = 0

    i = 2
    while i < M:
        word = S[i-3:i]
        if word == "IOI":
            IOIcnt += 1

            if IOIcnt >= N:
                total += 1
            i += 2
        else:
            IOIcnt = 0
            i += 1
    print(total)

    # TEMPLATE ###############################


def parr(arr: List[List[Union[str, int]]]) -> None:
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
