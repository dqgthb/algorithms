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

    global N, mat, blanks
    mat = [[int(i) for i in input().strip()] for _ in range(9)]

    # ######## INPUT AREA END ############
    # ####################################

    blanks = []
    for i , j in For(9, 9):
        if mat[i][j] == 0:
            blanks.append((i, j))
    N = len(blanks)
    try:
        solve(0)
    except:
        pass


def solve(n):
    if n == N:
        for arr in mat:
            print(''.join(map(str, arr)))
        raise "END"

    x, y = blanks[n]
    for i in range(1, 10):
        if check(x, y, i):
            mat[x][y] = i
            solve(n+1)
            mat[x][y] = 0


def check(x, y, v):

    for i in range(9):
        if mat[i][y] == v:
            return False

    for i in range(9):
        if mat[x][i] == v:
            return False


    bx = 3 * (x // 3)
    by = 3 * (y // 3)
    #print(bx, by)
    for i in range(3):
        for j in range(3):
            if mat[bx+i][by+j] == v:
                return False
    return True




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
