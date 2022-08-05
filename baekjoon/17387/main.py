# CP template Version 1.006
import os
import sys
import itertools
import collections
import string
# not for python < 3.9
# from functools import cmp_to_key, reduce, partial, cache
from functools import cmp_to_key, reduce, partial
from itertools import product
from collections import deque, Counter, defaultdict as dd
from math import log, log2, ceil, floor, gcd, sqrt
import math
from heapq import heappush, heappop
from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ####################################
    # ######## INPUT AREA BEGIN ##########

    ax, ay, bx, by = map(int, input().split())
    cx, cy, dx, dy = map(int, input().split())

    # ######## INPUT AREA END ############
    # ####################################

    accw = ccw(cx, cy, dx, dy, ax, ay)
    bccw = ccw(cx, cy, dx, dy, bx, by)
    cccw = ccw(ax, ay, bx, by, cx, cy)
    dccw = ccw(ax, ay, bx, by, dx, dy)
    #print(accw, bccw, cccw, dccw)

    if accw == bccw == cccw == dccw == 0:
        abD = (ax - bx) ** 2 + (ay - by) ** 2
        cdD = (cx - dx) ** 2 + (cy - dy) ** 2
        acD = (ax - cx) ** 2 + (ay - cy) ** 2
        adD = (ax - dx) ** 2 + (ay - dy) ** 2
        bcD = (bx - cx) ** 2 + (by - cy) ** 2
        bdD = (bx - dx) ** 2 + (by - dy) ** 2
        maxD = max(acD, adD, bcD, bdD)

        #print(abD, cdD, acD, adD, bcD, bdD)
        l = abD ** (1/2) + cdD ** (1/2)
        d = maxD ** (1/2)
        if l < d:
            print("0")
        else:
            print("1")
        return

    elif accw * bccw <= 0 and cccw * dccw <= 0:
        print("1")
    else:
        print("0")


def ccw(x1, y1, x2, y2, x3, y3):
    return x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1



# #############################################################################
# #############################################################################
# ############################## TEMPLATE AREA ################################
# #############################################################################
# #############################################################################

enu = enumerate


def argmax(arr):
    return max(enumerate(arr), key=lambda x: x[1])


def argmin(arr):
    return min(enumerate(arr), key=lambda x: x[1])


def For(*args):
    return itertools.product(*map(range, args))


def copy2d(mat):
    return [row[:] for row in mat]


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


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()
