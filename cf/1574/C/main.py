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

    global n, a, m, sum_
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    sum_ = sum(a)
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        ans = solve(x, y)
        print(ans)

    # ######## INPUT AREA END ############
    # ####################################


def solve(x, y):
    idx = bl(a, x)

    if x < a[0]:
        defense = sum_ - a[0]
        return max(y - defense, 0)

    elif x > a[n-1]:
        coin = x - a[n-1]
        defense = sum_ - a[n-1]
        return max(y - defense, 0) + coin

    elif a[idx] == x:
        defense = sum_ - a[idx]
        return max(y - defense, 0)

    else:
        coin = x - a[idx-1]
        defense = sum_ - a[idx-1]
        cand1 =  max(y - defense, 0) + coin

        defense = sum_ - a[idx]
        cand2 = max(y - defense, 0)

        return min(cand1, cand2)









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
