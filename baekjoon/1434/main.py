import os
import sys
import itertools
import collections
TEST = ''
DEBUG = False
if os.path.exists("i" + TEST):
    DEBUG = True
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)
input=sys.stdin.readline


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def ints(): return map(int, sys.stdin.readline().strip().split())


def main():
    N, M = (int(i) for i in input().split())

    box = [int(i) for i in input().split()]
    book = [int(i) for i in input().split()]

    wasted = 0
    boxIdx = 0
    bookIdx = 0
    boxlen = len(box)
    booklen = len(book)

    for i in range(len(box)):
        currBox = box[i]

        while bookIdx < booklen and currBox - book[bookIdx] >= 0:
            currBox -= book[bookIdx]
            bookIdx += 1

        wasted += currBox
    print(wasted)

if __name__ == "__main__":
    main()