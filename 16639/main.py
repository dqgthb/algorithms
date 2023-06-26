# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
import itertools
import re
from sys import stdin, argv
from os import path

# from collections import deque
# from heapq import heappush, heappop
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br


def main() -> None:
    # sys.setrecursionlimit(10**9)
    pass

    N = int(input())
    expression = input().strip()

    arr = re.split(r"([\+\*\-])", expression)

    nums = [e for i, e in enumerate(arr) if i % 2 == 0]
    ops = [e for i, e in enumerate(arr) if i % 2 == 1]

    print(nums)
    print(ops)

    for p in itertools.permutations(range(len(ops))):
        print(p)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
