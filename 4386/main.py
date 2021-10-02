# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
import itertools
#from itertools import product
#import collections
#from collections import deque, Counter, defaultdict as dd
import math
from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, p, S
    N = int(input())
    p = []
    for _ in range(N):
        x, y = map(float, input().split())
        p.append((x, y))

    # ######## INPUT AREA END ############

    S = [i for i in range(N)]

    p.sort()

    edges = []
    for i in range(N):
        x, y = p[i]
        minDist = 10**15

        for j in range(i+1, N):
            xj, yj = p[j]
            dist = d(x, y, xj, yj)
            minDist = min(minDist, dist)
            edges.append((dist, i, j))
            if x - xj >= minDist:
                break
    edges.sort()

    vis = [False] * N

    sum_ = 0
    for dist, i, j in edges:
        pi = find(i)
        pj = find(j)
        if pi == pj: continue
        else:
            sum_ += dist
            union(i, j)
    print(sum_)


def d(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def find(x):
    if S[x] == x: return x
    else:
        S[x] = find(S[x])
        return S[x]


def union(x, y):
    px = find(x)
    py = find(y)
    if px == py: return
    else:
        S[y] = px
        union(px, py)



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