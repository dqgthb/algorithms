# Python Competitive Programming Template (updated 2022-08-05)
# Created by dqgthb

# from collections import deque
# from heapq import heappush, heappop

# from functools import cmp_to_key, reduce, partial
# from collections import Counter, defaultdict as dd
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br


from collections import deque
from typing import Callable, List, Union
input: Callable[[], str]


class StepFreq:
    def __init__(self, step, freq):
        self.step = step
        self.freq = freq

    def __str__(self):
        return f"{self.step}, {self.freq}"


def main() -> None:
    init()
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    N, K = map(int, input().split())
    DP = [None for _ in range(200000)]

    # ######## INPUT AREA END ############

    DP[N] = StepFreq(0, 1)

    dq = deque()
    dq.append((N, 0))

    while dq:
        idx, step = dq.popleft()
        freq = DP[idx].freq

        for newIdx in (idx-1, idx+1, idx*2):
            if 0 <= newIdx < 200000:
                stepFreq = DP[newIdx]
                if stepFreq is not None:
                    if stepFreq.step > step + 1:
                        stepFreq.step = step + 1
                        stepFreq.freq = freq
                        dq.append((newIdx, step+1))
                    elif stepFreq.step == step + 1:
                        stepFreq.freq += freq
                else:
                    DP[newIdx] = StepFreq(step+1, freq)
                    dq.append((newIdx, step+1))

    print(DP[K].step, "\n", DP[K].freq, sep="")


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
