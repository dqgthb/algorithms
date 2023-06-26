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
    pass

    global S, E, N
    S = input().strip()
    E = input().strip()
    N = len(E)

    stack = []

    for i, e in enumerate(S):
        stack.append(e)

        while True:
            if len(stack) >= N:
                if ''.join(stack[-N:]) == E:
                    for _ in range(N):
                        stack.pop()
                    continue
            break
    if stack:
        print(''.join(stack))
    else:
        print("FRULA")


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()