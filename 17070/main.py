# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from sys import stdin, argv
from os import path

from functools import cache


def main() -> None:
    # sys.setrecursionlimit(10**9)
    global N, A

    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    a1 = dp(N - 1, N - 1, 0)
    a2 = dp(N - 1, N - 1, 1)
    a3 = dp(N - 1, N - 1, 2)

    # print(a1, a2, a3)

    print(a1 + a2 + a3)


# k = 0: horizontal
# k = 1: vertical
# k = 2: diagonal
@cache
def dp(i, j, k):
    if (i, j, k) == (0, 1, 0):
        return 1

    if not (0 <= i < N) or not (0 <= j < N):
        return 0

    if A[i][j] == 1:
        return 0

    ans = 0
    if k == 0:
        ans += dp(i, j - 1, 0)
        ans += dp(i, j - 1, 2)

    elif k == 1:
        ans += dp(i - 1, j, 1)
        ans += dp(i - 1, j, 2)

    else:  # k == 2
        if A[i - 1][j] == 1:
            return 0
        if A[i][j - 1] == 1:
            return 0

        ans += dp(i - 1, j - 1, 0)
        ans += dp(i - 1, j - 1, 1)
        ans += dp(i - 1, j - 1, 2)

    return ans


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()


# modern dp
@cache
def DFS(x, y, z):
    # basebase

    # main logic
    # calculation

    return ans
