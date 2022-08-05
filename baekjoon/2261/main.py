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

    global N, points
    N = int(input())
    points = [tuple(int(i) for i in input().split()) for _ in range(N)]
    points = list(set(points))
    if N != len(points):
        print(0)
        return
    points.sort()
    ans = dc(0, N-1)
    print(ans)

    # ######## INPUT AREA END ############
    # ####################################


def distance(idx1, idx2):
    x1, y1 = points[idx1]
    x2, y2 = points[idx2]

    return (y2-y1)**2 + (x2-x1)**2


def dc(start, end):
    mid = (start + end) // 2

    if start == end:
        return 10 ** 15
    elif end - start == 1:
        return distance(start, end)
    elif end - start == 2:
        d1 = distance(start, mid)
        d2 = distance(end, mid)
        d3 = distance(start, end)
        return min(d1, d2, d3)


    c1 = dc(start, mid)
    c2 = dc(mid+1, end)
    minDSqr = min(c1, c2)
    ps = []
    mx, my = points[mid]

    for i in range(start, end+1):
        x, y = points[i]
        if (x - mx) ** 2 < minDSqr:
            ps.append(i)

    ps.sort(key = lambda x:points[x][1])

    for i in range(len(ps)-1):
        x1, y1 = points[ps[i]]
        for j in range(i, len(ps)):
            x2, y2 = points[ps[j]]
            if (y2 - y1) ** 2 >= minDSqr:
                break

            if x1 <= mx and x2 <= mx:
                continue

            if x1 > mx and x2 > mx:
                continue

            dist = (y2-y1)**2 + (x2-x1)**2
            minDSqr = min(minDSqr, dist)
    return minDSqr




    for i in range(len(lps)):
        lx, ly = points[lps[i]]
        for j in range(len(rps)):
            rx, ry = points[rps[j]]
            if ry > ly and (ry - ly)**2 > minDSqr:
                break

            distSqr = (rx - lx) ** 2 + (ry - ly) ** 2

            if distSqr < minDSqr:
                minDSqr = distSqr
    return minDSqr



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
