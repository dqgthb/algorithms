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
    mat = [list(map(int, input().split())) for _ in range(N)]

    # ######## INPUT AREA END ############
    # ####################################
    parr(mat)
    moveUp(0)
    moveUp(1)
    moveUp(2)
    parr(mat)


def moveRight(row):
    prevCol = None

    for currCol in range(N-1, -1, -1):
        currNo = mat[row][currCol]

        if currNo == 0:
            pass
        else:
            if prevCol is None:
                mat[row][currCol] = 0
                mat[row][N-1] = currNo
                prevCol = N-1
            else:
                if mat[row][prevCol] == currNo:
                    mat[row][prevCol] *= 2
                    mat[row][currCol] = 0
                else:
                    mat[row][currCol] = 0
                    mat[row][prevCol-1] = currNo
                    prevCol -= 1


def moveLeft(row):
    prevCol = None

    for currCol in range(N):
        currNo = mat[row][currCol]

        if currNo == 0:
            pass
        else:
            if prevCol is None:
                mat[row][currCol] = 0
                mat[row][0] = currNo
                prevCol = 0
            else:
                if mat[row][prevCol] == currNo:
                    mat[row][prevCol] *= 2
                    mat[row][currCol] = 0
                else:
                    mat[row][currCol] = 0
                    mat[row][prevCol+1] = currNo
                    prevCol += 1


def moveUp(col):
    prevRow = None

    for currRow in range(N):
        currNo = mat[currRow][col]

        if currNo == 0:
            pass
        else:
            if prevRow is None:
                mat[currRow][col] = 0
                mat[0][col] = currNo
                prevRow = 0
            else:
                if mat[prevRow][col] == currNo:
                    mat[prevRow][col] *= 2
                    mat[currRow][col] = 0
                else:
                    mat[currRow][col] = 0
                    mat[prevRow+1][col] = currNo
                    prevRow += 1


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
