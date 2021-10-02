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
from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    n = int(input())
    p = []
    for _ in range(n):
        x, y = map(float, input().split())
        p.append((x, y))

    # ######## INPUT AREA END ############

    pq = []
    vis = [False] * n
    vis[0] = True
    x0, y0 = p[0]
    for i in range(1, n):
        x, y = p[i]
        dist = (x - x0) ** 2 + (y - y0) ** 2
        dist = sqrt(dist)
        heappush(pq, (dist, i))
    cost = 0
    num = 0

    while pq:
        d, i = heappop(pq)
        if vis[i]:
            continue
        vis[i] = True
        cost += d
        x, y = p[i]
        num += 1
        if num == n:
            break

        for j in range(n):
            if j != i and not vis[j]:
                xj, yj = p[j]
                distIJ = (x - xj) ** 2 + (y - yj) ** 2
                distIJ = sqrt(distIJ)
                heappush(pq, (distIJ, j))

    print(cost)


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