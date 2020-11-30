import os
import sys
import itertools
import collections

DEBUG = False
if len(sys.argv) == 1:
    inputFile = "i"
    if os.path.exists(inputFile):
        DEBUG = True
        sys.stdin = open(inputFile)

    if os.path.exists("a"):
        sys.stdout = open("o", "w")

elif len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
else:
    assert False, "too many arguments"
input=sys.stdin.readline


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def ints(): return map(int, sys.stdin.readline().strip().split())


def main():
    arr = [int(input().strip()) for _ in range(10)]
    cum = [0 for _ in range(len(arr) + 1)]
    for i in range(1, len(cum)):
        cum[i] = cum[i-1] + arr[i-1]

    for i,e in enumerate(cum):
        cum[i] -= 100

    m = cum[0]
    for i in cum:
        if abs(m) >= abs(i):
            m = i

    print(100 + m)


if __name__ == "__main__":
    main()