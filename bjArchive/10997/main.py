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

    global N, mat
    N = int(input())
    W = 4 * N - 3
    H = 4 * N - 1

    mat = Mat(H, W, ' ')

    # ######## INPUT AREA END ############
    # ####################################


    if N == 1:
        print("*")
        return
    draw(0, 0, N)

    mat[1] = "*"


    pmat()




def pmat():
    for arr in mat:
        print(''.join(arr))


def draw(x, y, n):

    if n == 1:
        mat[x][y] = '*'
        return

    if n == 2:
        mat[x+3][y+2] = '*'
        mat[x+2][y+3] = '*'
        mat[x+4][y+2] = '*'
        pass


    for i in range(4 * n - 3):
        mat[x][y+i] = '*'

    for i in range(4 * n - 1):
        mat[x+i][y] = '*'

    for i in range(4 * n - 3):
        mat[x+4 * n - 2][y+i] = '*'


    for i in range(2, 4 * n - 1):
        mat[x+i][y + 4 * n - 4] = '*'

    mat[x+2][y+4 * n - 5] = '*'


    draw(x+2, y+2, n-1)









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
