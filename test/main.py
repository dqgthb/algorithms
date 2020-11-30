import os
import sys
import itertools
import collections

TEST = ''
if os.path.exists("i"+TEST):
    sys.stdin = open("i"+TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w")


def printe(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def pfast(*args, end = "\n", sep = ' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


def input(): return sys.stdin.readline()


def main():
    pfast("hello", "world", 5, 5, sep ='')


if __name__ == "__main__":
    main()