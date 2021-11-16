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

    global N, p, p0
    N = int(input())
    p = []
    for _ in range(N):
        x, y = map(int, input().split())
        p.append((x, y))

    # ######## INPUT AREA END ############
    # ####################################


    # Gramham Scan algorithm or Jarvis March algorithm?
    # Let's use Graham
    # get the lowest point
    p.sort(key = lambda point: point[1], reverse=True) # by y
    p.sort(key = lambda point: point[0]) # by x

    p0 = min(p, key = lambda point:point[1])

    # get angle = atan2(y / x) of all points and sort
    p.sort(key = lambda point: getAngle(p0, point))

    for point in p:
        dprint(point, getAngle(p0, point))

    # loop through sorted points, calculate ccw. Put them into stack.
    stack = [p[0], p[1]]
    idx = 2
    dprint(p)

    for point in p[2:]:
        dprint(point)
        while True:
            if CCW(stack[-2], stack[-1], point) > 0:
                stack.append(point)
                break
            else:
                stack.pop()
                if len(stack) == 1:
                    stack.append(point)
                    break
        dprint(stack)

    if CCW(stack[-2], stack[-1], p0) <= 0:
        stack.pop()
    dprint(stack)


    print(len(stack))

    # If CCW is negative, pop. If CCW is the same, choose the one with -


def getAngle(a, b):
    xa, ya = a
    xb, yb = b
    return math.atan2(yb - ya, xb - xa)


def CCW(a, b, c):
    xa, ya = a
    xb, yb = b
    xc, yc = c

    crossProduct = (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)

    if crossProduct > 0:
        return 1
    elif crossProduct == 0:
        return 0
    else:
        return -1




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
