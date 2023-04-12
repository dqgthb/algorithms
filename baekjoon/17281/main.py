# Python Competitive Programming Template (updated 2022-08-05)
# Created by dqgthb

# from collections import deque
# from heapq import heappush, heappop

# from functools import cmp_to_key, reduce, partial
# from collections import Counter, defaultdict as dd
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br


from itertools import permutations
from typing import Callable, List, Tuple

input: Callable[[], str]
Num: int
Mat: List[List[int]]


def main() -> None:
    init()
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global Num, Mat
    Num = int(input())
    Mat = [[int(i) for i in input().split()] for _ in range(Num)]

    # ######## INPUT AREA END ############

    max_ = 0
    for seq in permutations(range(1, 9)):
        max_ = max(max_, game(seq))
    print(max_)

    # TEMPLATE ###############################


def game(seq: Tuple[int, ...]) -> int:
    # (3, 4, 1 ...) 3rd, 4th, 1st indexed players play in a sequence
    playerSeq: List[int] = [*seq[:3]] + [0] + [*seq[3:]]

    global Num, Mat
    sum_: int = 0
    seqIdx: int = 0
    f: bool
    s: bool
    t: bool

    for inning in range(Num):
        out = 0
        f, s, t = False, False, False

        while out < 3:

            performance = Mat[inning][playerSeq[seqIdx]]

            if performance == 0:
                out += 1

            elif performance == 1:
                sum_ += 1 if t else 0
                f, s, t = True, f, s

            elif performance == 2:
                sum_ += 1 if t else 0
                sum_ += 1 if s else 0
                f, s, t = False, True, f

            elif performance == 3:
                sum_ += 1 if t else 0
                sum_ += 1 if s else 0
                sum_ += 1 if f else 0
                f, s, t = False, False, True

            elif performance == 4:
                sum_ += 1
                sum_ += 1 if t else 0
                sum_ += 1 if s else 0
                sum_ += 1 if f else 0
                f, s, t = False, False, False

            seqIdx = (seqIdx + 1) % 9
    return sum_


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
