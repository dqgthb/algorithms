# CP template Version 1.006
import os
import sys
import itertools
import collections
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
    global N, H
    N, H = map(int, input().split())
    # Stalagmite: suksoon (bottom up)
    # Stalactite: jongyoosuk (top down)

    up = []
    down = []

    downSwitch = True
    for _ in range(N):
        if downSwitch:
            down.append(int(input()))
            downSwitch = not downSwitch
        else:
            up.append(int(input()))
            downSwitch = not downSwitch

    # ######## INPUT AREA END ############
    # ####################################

    up.sort()
    down.sort()

    '''
    max_ = 0
    maxCount = 0
    for h in range(H):
        cand = encounterBothBisect(up, down, h)
        if cand > max_:
            max_ = cand
            maxCount = 1
        elif cand == max_:
            maxCount += 1
    print(max_, maxCount)
    '''

    for h in range(H):
        print(upEncounterBisect(up, h), end=' ')
    print()
    for h in range(H):
        print(encounterBisect(down, h), end=' ')



def upEncounterBisect(up, height):
    return encounterBruteforce(up, H-height+1)


def encounterBothBisect(up, down, height):
    return upEncounterBisect(up, height) + encounterBisect(down, height)


def encounterBisect(arr, height):
    firstEncounter = bl(arr, height, 0, len(arr))
    return len(arr) - firstEncounter


def encounterBothBruteforce(up, down, height):
    count = 0
    for i in up:
        if height > H - i:
            count += 1

    for i in down:
        if height <= i:
            count += 1
    return count


def encounterBruteforce(arr, height):
    count = 0
    for i in arr:
        if height <= i:
            count += 1
    return count


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
