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
    sys.setrecursionlimit(10**9)
    # ####################################
    # ######## INPUT AREA BEGIN ##########

    global V, E, G, rG
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]
    rG = [[] for _ in range(V)]
    for _ in range(E):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        G[A].append(B)
        rG[B].append(A)

    # ######## INPUT AREA END ############
    # ####################################

    global stack, visited, scc
    stack = []
    visited = [False] * V
    for v in range(V):
        if not visited[v]:
            dfs(v)

    ans = []
    visited = [False] * V
    stack.reverse()
    for v in stack:
        if not visited[v]:
            scc = []
            rdfs(v)
            scc.sort()
            ans.append(scc)
    ans.sort()

    print(len(ans))
    for scc in ans:
        print(' '.join(map(lambda x:str(x+1), scc)), -1)


def rdfs(v):
    visited[v] = True
    scc.append(v)
    for nv in rG[v]:
        if not visited[nv]:
            rdfs(nv)


def dfs(v):
    visited[v] = True
    for nv in G[v]:
        if not visited[nv]:
            dfs(nv)
    stack.append(v)








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
