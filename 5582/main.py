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
    S = input().strip()
    SN = len(S)
    T = input().strip()
    TN = len(T)

    T = "," * (SN - 1) + T + "." * (SN - 1)
    maxCount = 0

    for i in range(TN + SN - 1):
        count = 0
        for j in range(SN):
            s = S[j]
            t = T[i + j]
            # print(s, t, end=" ")

            if s == t:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 0
        # print()
    print(maxCount)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
