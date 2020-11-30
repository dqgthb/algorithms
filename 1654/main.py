import os
import sys
import itertools
import collections
TEST = ''
if os.path.exists("i" + TEST):
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)


def printe(*args,**kwargs):
    print(*args, **kwargs, file=sys.stderr)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


def input(): return sys.stdin.readline()


def main():
    K, N = (int(i) for i in input().split())

    arr = [int(input().strip()) for _ in range(K)]

    left = 1
    right = 2 ** 31 - 1

    max_ = 0
    cand = 1
    while left <= right:
        mid = (left + right) // 2

        count = 0
        for i in arr:
            count += i // mid
        if count < N:
            right = mid - 1
        else:
            left = mid + 1
            max_ = count
            cand = mid
    print(cand)


if __name__ == "__main__":
    main()