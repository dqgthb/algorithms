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

    global a, b, dp, la, lb
    a = input().strip()
    la = (len(a))
    b = input().strip()
    lb= (len(b))
    dp = Mat(len(a), len(b))

    # ######## INPUT AREA END ############
    # ####################################

    ans = solve(0, 0)
    print(ans)
    parr(dp)
    str_ = ""
    if ans != 0:
        x, y = 0, 0
        while x != la and y != lb:
            cur = dp[x][y]
            if 0 <= x+1 < la and dp[x+1][y] == cur:
                x += 1
                continue
            if 0 <= y+1 < lb and dp[x][y+1] == cur:
                y += 1
                continue

            if x + 1 < la and y + 1 < lb:
                str_ += a[x]
                x+=1
                y+=1
            print(x, y)



def solve(x, y):
    if x == la or y == lb:
        return 0
    if dp[x][y] is not None:
        return dp[x][y]

    cand1 = solve(x+1, y)
    cand2 = solve(x, y+1)
    cand3 = 0
    if a[x] == b[y]:
        cand3 = 1 + solve(x+1, y+1)
    ans = max(cand1, cand2, cand3)
    dp[x][y] = ans
    return dp[x][y]







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
