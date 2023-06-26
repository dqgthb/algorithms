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

    global N, A, DP, T

    N = int(input())
    A = [int(i) for i in input().split()]
    T = A[N - 1]

    DP = {}

    count = solve(0, 0)

    print(DP)

    print(count)


def solve(i, partialSum):
    if i == N - 1:
        if partialSum == T:
            return 1
        return 0

    if (i, partialSum) in DP:
        print("check", i, partialSum)
        return DP[(i, partialSum)]

    ret = 0
    if 0 <= partialSum - A[i] <= 20:
        ret += solve(i + 1, partialSum - A[i])

    if 0 <= partialSum + A[i] <= 20:
        ret += solve(i + 1, partialSum + A[i])

    DP[(i, partialSum)] = ret
    return ret


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
