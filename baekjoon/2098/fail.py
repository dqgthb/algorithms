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

    dp = nDim(N, 2 ** N)

    ans = 10 ** 15

    '''
    for i in range(2 ** N):
        for j in range(N):
            solve(j, j, i)
    '''

    for i in range(N):
        cand = solve(i, i, (2 ** N - 1) & ~(2 ** i))
        print(cand)
        ans = min(cand, ans)
    #ans = solve(0, 0, 2 ** N - 1 & ~(2 ** 0))
    print(ans)

    parr(dp)


    # ######## INPUT AREA END ############
    # ####################################


def solve(from_, to, mustVisit):
    print(from_, to, format(mustVisit, '04b'))

    ret = dp[from_][mustVisit]
    if ret is not None:
        return ret

    ret = 10 ** 15

    mask = mustVisit
    idx = 0
    while mask:
        mask, r = divmod(mask, 2)
        if idx == from_ or idx == to:
            idx += 1
            continue

        if dist[from_][idx] == 0:
            idx += 1
            continue

        if r == 1:
            newMustVisit = mustVisit & ~(2**idx)
            if newMustVisit == 0:
                if dist[idx][to] != 0:
                    ans = dist[from_][idx] + dist[idx][to]
                    dp[from_][0] = ans
                    return ans
                else:
                    dp[from_][0] = 10 ** 15
                    return ans
            else:
                cand = dist[from_][idx] + solve(idx, to, newMustVisit)
            ret = min(ret, cand)
            print("ret updated to", ret)
        idx += 1
    dp[from_][mustVisit] = ret
    return ret





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
