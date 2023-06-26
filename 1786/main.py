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
    global T, P, TN, PN
    T = input()[:-1]
    P = input()

    TN = len(T)
    PN = len(P)

    D = buildLPS(P)
    # print(D)

    global cnt, lst
    cnt = 0
    lst = []

    kmp(T, P, D)

    print(cnt)
    print(" ".join(str(i - PN + 2) for i in lst))


def kmp(T, P, D):
    global cnt
    j = 0
    for i in range(TN):
        while j > 0 and T[i] != P[j]:
            j = D[j - 1]

        if T[i] == P[j]:
            j += 1
            if j == PN:
                cnt += 1
                lst.append(i)
                j = D[j - 1]


def buildLPS(P):
    PN = len(P)
    D = [0 for _ in range(PN)]

    j = 0
    for i in range(1, PN):
        while j > 0 and P[i] != P[j]:
            j = D[j - 1]

        if P[i] == P[j]:
            j += 1
            D[i] = j
    return D


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
