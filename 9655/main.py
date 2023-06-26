# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from functools import cache
from sys import stdin, argv
from os import path


def main() -> None:
    # sys.setrecursionlimit(10**9)
    N = int(input())

    for i in range(N):
        print(i, dp(i))


@cache
def dp(n):
    if n <= 3:
        return n % 2 == 1
    else:
        return not (dp(n - 1) and dp(n - 3))


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
