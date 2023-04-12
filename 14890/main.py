import sys
import logging
import os


from enum import Enum


class State(Enum):
    SAME = 0
    MINUS1 = 1
    PLUS1 = 2


def validate_list(lst):
    same = 1

    state = State.SAME

    for i in range(N - 1):
        cur = lst[i]
        nxt = lst[i + 1]

        if state == State.SAME:

            if cur == nxt:
                same += 1

            elif cur == nxt + 1:
                state = State.PLUS1
                continue

            elif cur == nxt - 1:
                state = State.MINUS1
                continue

            else:
                return False


def solve():
    i = 0
    while i < N:
        j = 0
        while j < N:

            j += 1
        print()
        i += 1


def main():
    global N, L, map_

    logging.basicConfig(level=logging.INFO)

    inputFile = sys.stdin
    if os.path.exists("i.txt"):
        inputFile = "i.txt"

    with open(inputFile) as f:
        N, L = map(int, f.readline().split())

        map_ = [[int(i) for i in f.readline().split()] for _ in range(N)]
        logging.info("\n%s", "\n".join(map(str, map_)))

        solve()


if __name__ == "__main__":
    main()
