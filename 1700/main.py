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

    global N, K
    N, K = map(int, input().split())
    A = [int(i) - 1 for i in input().split()]

    count = 0

    tab = set()

    for i, e in enumerate(A):

        if e in tab:
            continue

        if len(tab) < N:
            tab.add(e)

        else:
            idx, t = leastUsed(tab, A[i:])
            tab.remove(idx)
            tab.add(e)
            count += 1
    print(count)


def leastUsed(tab, schedule):
    global K
    recentUsed = [0 for _ in range(K)]
    for i in tab:
        recentUsed[i] = 10 ** 9

    for i, e in enumerate(schedule):
        if e in tab:
            recentUsed[e] = min(recentUsed[e], i)

    return max(enumerate(recentUsed), key=lambda x: x[1])


def testLeastUsed():
    x = leastUsed((2, 3), [2, 3, 1, 2, 7])


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
    testLeastUsed()
