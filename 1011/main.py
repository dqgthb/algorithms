# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from collections import deque
from sys import stdin, argv
from os import path


def main() -> None:
    # sys.setrecursionlimit(10**9)

    T = int(input())

    for _ in range(T):
        global X, Y
        X, Y = map(int, input().split())

        solve()


def solve():

    dq = deque([X])
    s


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
