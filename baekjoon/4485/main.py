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

    global N, mat, D
    while True:

        N = int(input())
        if N == 0:
            return
        mat = [list(map(int, input().split())) for _ in range(N)]
        D = Mat(N, N)

        D[0][0] = mat[0][0]

        print(dp(0, 0))
        print(dp(0, 1))

        print(dp(N-1, N-1))

    # ######## INPUT AREA END ############



dir = ((-1, 0), (1, 0), (0, 1), (0, -1))
def dp(x, y):

    if D[x][y] is not None:
        return D[x][y]

    mx, my = -1, -1
    min_ = 10**9
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            d = dp(nx, ny)
            if min_ > d:
                min_ = d
                mx = nx
                ny = ny
    D[x][y] = min_ + mat[x][y]
    return D[x][y]

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