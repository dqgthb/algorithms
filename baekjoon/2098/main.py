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

    global N, dist, dp
    N = int(input())

    dist = [list(map(int, input().split())) for _ in range(N)]
    for i, j in For(N, N):
        if dist[i][j] == 0:
            dist[i][j] = 10 ** 15

    dp = Mat(N, 2 ** N)
    mask = 2 ** N - 1
    ans = 10 ** 15
    '''
    for i in range(3,N):
        notVisited = mask & ~(2 ** i)
        cand = tsp(i, i, notVisited)
        print(cand)
        ans = min(cand, ans)
        parr(dp)
    '''
    notVisited = mask & ~(2 ** 0)
    ans = tsp(0, 0, notVisited)
    print(ans)



    # ######## INPUT AREA END ############
    # ####################################


def tsp(start, from_, notVisited):
    if notVisited == 0:
        return dist[from_][start]

    if dp[from_][notVisited] is not None:
        print("dp!", from_, notVisited)
        return dp[from_][notVisited]


    ans = 10 ** 15
    cand = 10 ** 15
    mask = notVisited
    for i in range(N):
        mask, r = divmod(mask, 2)
        if r == 1:
            cand = dist[from_][i] + tsp(start, i, notVisited & ~(2 ** i))
            ans = min(cand, ans)
    dp[from_][notVisited] = ans
    return ans





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
