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

    A = input().strip()
    B = input().strip()
    solve(A, B)

    # ######## INPUT AREA END ############


def solve(A, B):
    Aint: int = int(A)

    for bchar in reversed(B):
        print(Aint * int(bchar))
    Bint: int = int(B)

    print(Aint * Bint)

    # TEMPLATE ###############################


def parr(arr):
    print('\n'.join(str(i) for i in arr))


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
