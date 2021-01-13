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
from typing import Deque, Any, Optional

def main(f = None):
    init(f)
    N: int
    R: int
    q: int
    N, R, Q = map(int, input().split())
    R -= 1
    g:list[list[int]] = [[] for _ in range(N)]
    for _ in range(N-1):
        U:int 
        V:int
        U, V = map(lambda x: int(x)-1, input().split())
        g[U].append(V)
        g[V].append(U)
    parentOf = [-1 for _ in range(N)]
    numOfChildrenOf: list[Optional[int]] = [None for _ in range(N)]

    dq: Deque[Any] = deque()
    dq.append((R, -1))
    
    # find parents of each node
    while dq:
        node, parent = dq.popleft()
        for child in g[node]:
            if child == parent: continue
            parentOf[child] = node
            dq.append((child, node))
    for i in range(N):
        print("parent of", i+1, "is", parentOf[i]+1)
    
    # find number of children of each node
    def numOfChildren(node: int) -> Optional[int]:
        if numOfChildrenOf[node] is not None:
            return numOfChildrenOf[node]
        
        if len(g[node]) == 1 and g[node][0] == parentOf[node]:
            numOfChildrenOf[node] = 0
            return 0
        
        sum_ = 0
        for child in g[node]:
            if child == parentOf[node]: continue
            sum_ += numOfChildren(node) + 1
        return sum_
    


    def solve(q:int) -> int:

        return 0

    for _ in range(Q):
        q = int(input())
        solve(q)

DEBUG = False

def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
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