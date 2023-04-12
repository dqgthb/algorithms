import sys
from typing import List
DEBUG = False
DEBUG = True
if DEBUG:
    sys.stdin = open("i", "r")


def print_(*args: List[int]) -> None:
    if DEBUG:
        print(*args)


memoi = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]


def main() -> None:
    for line in sys.stdin:
        n = int(line.strip())
        print(memoi[n])


if __name__ == "__main__":
    main()
