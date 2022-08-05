# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
import itertools
#from itertools import product
#import collections
#from collections import deque, Counter, defaultdict as dd
#import math
from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())

    # ######## INPUT AREA END ############

    l1x, l1y = ax, ay
    r1x, r1y = bx, by

    l2x, l2y = cx, cy
    r2x, r2y = dx, dy

    d = 10 ** 15

    while True:
        p1x, p1y = getP(l1x, r1x), getP(l1y, r1y)
        q1x, q1y = getQ(l1x, r1x), getQ(l1y, r1y)
        p2x, p2y = getP(l2x, r2x), getP(l2y, r2y)
        q2x, q2y = getQ(l2x, r2x), getQ(l2y, r2y)
        pd = getDistance(p1x, p1y, p2x, p2y)
        qd = getDistance(q1x, q1y, q2x, q2y)

        if r1x == q1x:
            break

        if pd <= qd:
            r1x, r1y = q1x, q1y
            r2x, r2y = q2x, q2y
        elif pd >= qd:
            l1x, l1y = p1x, p1y
            l2x, l2y = p2x, p2y

        if d > min(pd, qd):
            d = min(pd, qd)

    print(sqrt(d))


def getP(l, r):
    return l + (r - l) / 3

def getQ(l, r):
    return l + 2 * (r - l) / 3

def getDistance(ax, ay, bx, by):
    return (bx - ax) ** 2 + (by - ay) ** 2


# TEMPLATE ###############################
enu = enumerate


def For(*args):
    return itertools.product(*map(range, args))


def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]


def nDim(*args, default=None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default=default) for _ in range(args[0])]


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


def init(f=None):
    global input
    input = sys.stdin.readline  # by default
    if os.path.exists("o"):
        sys.stdout = open("o", "w")
    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"):
                setStdin("in/i")
            elif os.path.isfile("i"):
                setStdin("i")
        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])
        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)


def pr(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()
