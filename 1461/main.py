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
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]

    if abs(min(A)) > max(A):
        for i, e in enumerate(A):
            A[i] = -e
    A.sort()

    pA = [i for i in A if i > 0]
    nA = [i for i in A if i < 0]
    nA.sort(reverse=True)

    A = pA

    sum_ = 0
    if pA:
        sum_ += A.pop()

        for _ in range(M - 1):
            if A:
                A.pop()

    while A:
        sum_ += 2 * A.pop()
        for _ in range(M - 1):
            if A:
                A.pop()

    A = nA
    while A:
        sum_ += abs(2 * A.pop())
        for _ in range(M - 1):
            if A:
                A.pop()

    print(sum_)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
