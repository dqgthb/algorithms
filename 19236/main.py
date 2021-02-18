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


di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ####################################
    # ######## INPUT AREA BEGIN ##########

    global mat, fish, si, sj
    mat = []
    for _ in range(4):
        arr = [int(i)-1 for i in input().split()]
        a = []
        for i in range(0, 8, 2):
            a.append([arr[i], arr[i+1]])
        mat.append(a)

    # ######## INPUT AREA END ############
    # ####################################

    fish = [None for _ in range(16)]
    for i, j in For(4, 4):
        val = mat[i][j]
        fish[val[0]] = (i, j)

    si, sj = 0, 0
    prey, sd = mat[si][sj]
    mat[si][sj] = [prey, sd]
    fish[prey] = [-1, None]
    print(fish)
    moveFish()
    parr(mat)

def moveFish():
    for i, j in fish:
        if i == -1:
            continue
        fishNum, d = mat[i][j]

        for _ in range(8):
            ni = di[d]
            nj = dj[d]

            if not (0 <= ni < 4 and 0 <= nj < 4):
                d = (d + 1) % 8
                continue
            if ni == si and nj == sj:
                d = (d + 1) % 8
                continue
            mat[i][j][1] = d
            swapFish(i, j, ni, nj)


def swapFish(i, j, ni, nj):
    fish1 = mat[i][j][0]
    fish2 = mat[ni][nj][0]
    mat[i][j], mat[ni][nj] = mat[ni][nj], mat[i][j]
    fish[fish1], fish[fish2] = fish[fish2], fish[fish1]

















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


# Mod #
class Mod:
    MOD = 10**9 + 7
    maxN = 5
    FACT = [0] * maxN
    INV_FACT = [0] * maxN

    @staticmethod
    def setMOD(n): Mod.MOD = n

    @staticmethod
    def add(x, y): return (x+y) % Mod.MOD

    @staticmethod
    def multiply(x, y): return (x*y) % Mod.MOD

    @staticmethod
    def power(x, y):
        if y == 0:
            return 1
        elif y % 2:
            return Mod.multiply(x, Mod.power(x, y-1))
        else:
            a = Mod.power(x, y//2)
            return Mod.multiply(a, a)

    @staticmethod
    def inverse(x):
        return Mod.power(x, Mod.MOD-2)

    @staticmethod
    def divide(x, y):
        return Mod.multiply(x, Mod.inverse(y))

    @staticmethod
    def allFactorials():
        Mod.FACT[0] = 1
        for i in range(1, Mod.maxN):
            Mod.FACT[i] = Mod.multiply(i, Mod.FACT[i-1])

    @staticmethod
    def inverseFactorials():
        n = len(Mod.INV_FACT)
        Mod.INV_FACT[n-1] = Mod.inverse(Mod.FACT[n-1])
        for i in range(n-2, -1, -1):
            Mod.INV_FACT[i] = Mod.multiply(Mod.INV_FACT[i+1], i+1)

    @staticmethod
    def coeffBinom(n, k):
        if n < k:
            return 0
        return Mod.multiply(Mod.FACT[n],
                            Mod.multiply(Mod.INV_FACT[k], Mod.INV_FACT[n-k]))

    @staticmethod
    def sum(it):
        res = 0
        for i in it:
            res = Mod.add(res, i)
        return res
# END Mod #


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
