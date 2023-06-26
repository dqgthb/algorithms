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
    K = int(input())
    A = [int(i) for i in input().split()]
    A.sort()

    diff = []
    for i in range(N - 1):
        diff.append(A[i + 1] - A[i])

    diff.sort()

    print(sum(diff[: N - K]))


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
