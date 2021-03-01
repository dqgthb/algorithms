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
    #sys.setrecursionlimit(10**9)
    # ####################################
    # ######## INPUT AREA BEGIN ##########

    global N, arr, M, S, E, DP
    N = int(input())
    arr = [int(i) for i in input().split()]
    M = int(input())
    DP = Mat(N, N)
    for i in range(N):
        DP[i][i] = True

    for i in range(N-1):
        DP[i][i+1] = arr[i] == arr[i+1]
    parr(DP)

    for i in range(N):
        for j in range(i+2, N):
            DP[i][j] = DP[i+1][j-1] and arr[i] == arr[j]

    for _ in range(M):
        S, E = map(lambda x: int(x) - 1, input().split())
        print(1 if DP[S][E] else 0)
    parr(DP)

    # ######## INPUT AREA END ############
    # ####################################

def dp(s, e):
    if DP[s][e] is not None:
        return DP[s][e]

    if s == e:
        val = True
    elif e - s == 1:
        val = arr[s] == arr[e]
    else:
        val = dp(s+1, e-1) and arr[s] == arr[e]
    DP[s][e] = val
    return val




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
