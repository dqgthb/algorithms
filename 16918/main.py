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
    global R, C, N, O
    R, C, N = map(int, input().split())
    O = [list(input().strip()) for _ in range(R)]

    for i in range(R):
        for j in range(C):
            O[i][j] = 3 if O[i][j] == "O" else 0

    test()

    for t in range(N):
        print(t)
        printO(O)
        reduceAndExplode(O)
        if t % 2 == 0:
            continue
        else:
            refill(O)

    printO(O)
    for o in O:
        print("".join(map(str, ("." if i == 0 else "O" for i in o))))


def refill(O):
    for i in range(R):
        for j in range(C):
            if O[i][j] == 0:
                O[i][j] = 3


D = ((-1, 0), (1, 0), (0, 1), (0, -1))


def reduceAndExplode(O):
    for i in range(R):
        for j in range(C):
            if O[i][j] > 0:
                O[i][j] -= 1
                if O[i][j] == 0:
                    # explode

                    for di, dj in D:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < R and 0 <= nj < C:
                            if O[ni][nj] != 1:
                                O[ni][nj] = 0


def printO(O):
    for o in O:
        print("".join(map(str, o)))


def test():
    pass


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
