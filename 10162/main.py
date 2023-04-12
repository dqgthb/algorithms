# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from sys import stdin, argv
from os import path


def main() -> None:
    # sys.setrecursionlimit(10**9)
    T = int(input())

    q1, r = divmod(T, 300)
    q2, r = divmod(r, 60)
    q3, r = divmod(r, 10)

    if r != 0:
        print(-1)
    else:
        print(q1, q2, q3)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
