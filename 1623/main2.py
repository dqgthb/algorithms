def main(f = None):
    init(f)
    cache = [[-1]*2 for _ in range(200000)]
    tree = [[] for _ in range(200000)]

    def sol(cur, flag):
        val = cache[cur][flag]
        if val != -1: return val
        cache[cur][flag] = 0

        if flag:
            cache[cur][flag] += cost[cur]
            for nxt in tree[cur]:
                cache[cur][flag] += sol(nxt, 0)
            return cache[cur][flag]
        
        else:
            for nxt in tree[cur]:
                cache[cur][flag] += max(sol(nxt, 0), sol(nxt, 1))
            return cache[cur][flag]

    N = int(input())
    tree = [[] for _ in range(N)]
    cost = [int(i) for i in input().split()]
    parentOf = [None] + [int(i)-1 for i in input().split()]
    for i in range(1, N):
        tree[parentOf[i]].append(i)
    
    print(sol(0, 1), sol(0, 0))

    def dfs(cur, flag, v):
        if flag:
            for nxt in tree[cur]:
                dfs(nxt, 0, v)
        else:
            for nxt in tree[cur]:
                if cache[nxt][0] > cache[nxt][1]:
                    dfs(nxt, 0, v)
                else:
                    dfs(nxt, 1, v)
                    v.append(nxt+1)

    withoutBoss = [0]
    dfs(0, 1, withoutBoss)
    withoutBoss.sort()
    print(*withoutBoss, -1)

    withBoss = []
    dfs(0, 0, withBoss)
    withBoss.sort()
    print(*withBoss, -1)




def For(*args):
    return itertools.product(*map(range, args))

def copy2d(mat):
    return [row[:] for row in mat]

def Mat(h, w, default = None):
    return [[default for _ in range(w)] for _ in range(h)]

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