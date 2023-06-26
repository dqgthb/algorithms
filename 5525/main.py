# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from sys import stdin, argv
from os import path


def main() -> None:
    # sys.setrecursionlimit(10**9)

    N = int(input())
    M = int(input())
    S = input().strip() + "$"

    streak = []

    cnt = 0
    STATE = 0
    for c in S:

        if STATE == 0:
            if c == "I":
                cnt = 0
                STATE = 1
            else:
                STATE = 0

        elif STATE == 1:
            if c == "I":
                cnt = 0
                STATE = 1
            else:
                STATE = 2

        elif STATE == 2:
            if c == "I":
                cnt += 1
                STATE = 3
            elif c == "O":
                streak.append(cnt)
                STATE = 0
            elif c == "$":
                streak.append(cnt)

        elif STATE == 3:
            if c == "I":
                streak.append(cnt)
                cnt = 0
                STATE = 1
            elif c == "O":
                STATE = 2
            elif c == "$":
                streak.append(cnt)

    sum_ = 0
    for s in streak:
        if s >= N:
            sum_ += s - N + 1
    print(sum_)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
