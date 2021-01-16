def main(f = None):
    init(f)
    H, W, K = map(int, input().split())
    mat = Mat(H, W, 'X')
    dp = Mat(H+1, W+1, 0)
    for _ in range(K):
        h, w, c = input().split()
        h, w = int(h), int(w)
        h -= 1
        w -= 1
        mat[h][w] = c
    mat[H-1][W-1] = 'X'

    dp[H][W-1] = 1
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if mat[i][j] == 'D':
                dp[i][j] = dp[i+1][j]
            elif mat[i][j] == 'R':
                dp[i][j] = dp[i][j+1]
            elif mat[i][j] == 'X':
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
    dp[H][W-1] = 0

    parr(dp)
    #for i in range(W-2)

def For(*args):
    return itertools.product(*map(range, args))

def copy2d(mat):
    return [row[:] for row in mat]

def Mat(h, w, default = None):
    return [[default for _ in range(w)] for _ in range(h)]

def nDim(*args, default = None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default = default) for _ in range(args[0])]

# CP template Version 1.005
import os
import sys
import itertools
import collections
from functools import cmp_to_key
from itertools import product
from collections import deque, Counter
from math import log, log2, ceil, floor
import math
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right

DEBUG = False

def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline

def init(f = None):
    global input
    input = sys.stdin.readline # by default
    if os.path.exists("o"): sys.stdout = open("o", "w")
    if f is not None: setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"): setStdin("in/i")
            elif os.path.isfile("i"): setStdin("i")
        elif len(sys.argv) == 2: setStdin(sys.argv[1])
        else: assert False, "Too many sys.argv: %d" % len(sys.argv)

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
        if y == 0: return 1
        elif y % 2: return Mod.multiply(x, Mod.power(x, y-1))
        else:
            a = Mod.power(x, y//2)
            return Mod.multiply(a, a)

    @staticmethod
    def inverse(x): return Mod.power(x, Mod.MOD-2)

    @staticmethod
    def divide(x, y): return Mod.multiply(x, Mod.inverse(y))

    @staticmethod
    def allFactorials():
        Mod.FACT[0] = 1
        for i in range(1, Mod.maxN): Mod.FACT[i] = Mod.multiply(i, Mod.FACT[i-1])

    @staticmethod
    def inverseFactorials():
        n = len(Mod.INV_FACT)
        Mod.INV_FACT[n-1] = Mod.inverse(Mod.FACT[n-1])
        for i in range(n-2, -1, -1): Mod.INV_FACT[i] = Mod.multiply(Mod.INV_FACT[i+1], i+1)

    @staticmethod
    def coeffBinom(n, k):
        if n < k: return 0
        return Mod.multiply(Mod.FACT[n], Mod.multiply(Mod.INV_FACT[k], Mod.INV_FACT[n-k]))
    
    @staticmethod
    def sum(it):
        res = 0
        for i in it: res = Mod.add(res, i)
        return res
# END Mod #

def dprint(*args):
    if DEBUG: print(*args)

def pfast(*args, end = "\n", sep=' '): sys.stdout.write(sep.join(map(str, args)) + end)

def parr(arr):
    for i in arr:
        print(i)

if __name__ == "__main__":
    main()