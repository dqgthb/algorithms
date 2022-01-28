# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, M, A, connected, P
    N, M = map(int, input().split())
    A = []
    P = [i for i in range(N)]
    for _ in range(N):
        a, b = map(int, input().split())
        A.append((a, b))

    #connected = []
    for _ in range(M):
        a, b = map(int, input().split())
        union(a-1, b-1)

    E = []
    for i in range(N):
        for j in range(i+1, N):
            E.append((getDistance(A[i], A[j]), i, j))

    E.sort()

    totalDistance = 0
    for d, i, j in E:
        if find(i) != find(j):
            union(i, j)
            totalDistance += d

    print('{:.2f}'.format(round(totalDistance, 2)))


def getDistance(a, b):
    x, y = a
    xx, yy = b
    return ((xx - x) ** 2 + (yy - y) ** 2) ** (0.5)


def find(x):
    if x == P[x]:
        return x
    else:
        px = find(P[x])
        P[x] = px
        return px


def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        P[px] = P[py] = px if px < py else py


    # ######## INPUT AREA END ############


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