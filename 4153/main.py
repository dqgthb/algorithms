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
    for line in sys.stdin:
        line = line.strip()
        if line == "0 0 0":
            break
        ls = [int(i) for i in line.split()]
        ls.sort()
        if ls[0] ** 2 + ls[1] ** 2 == ls[2] ** 2:
            pfast("right")
        else:
            pfast("wrong")


if __name__ == "__main__":
    main()