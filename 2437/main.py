# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from sys import stdin, argv
from os import path


def main() -> None:
    # sys.setrecursionlimit(10**9)
    N = int(input())

    arr = [int(i) for i in input().split()]

    arr.sort()

    sum_ = 0

    for i in arr:
        if i > sum_ + 1:
            break
        sum_ += i
    print(sum_ + 1)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
