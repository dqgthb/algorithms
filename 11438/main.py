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
    sys.setrecursionlimit(2 * 10**6)
    # ####################################
    # ######## INPUT AREA BEGIN ##########

    global N, g, depth, parent, visited, lN
    N = int(input())
    lN = ceil(log2(N))+1
    g = [[] for _ in range(N)]
    depth = [None] * N

    # parent[A][B] = A's 2**B th parent
    parent = [[None] * lN for _ in range(N)]
    visited = [False] * N

    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    visited[0] = True
    depth[0] = 0
    parent[0][0] = None
    dfs(0, 0)

    for i in range(1, lN):
        for j in range(1, N):
            half = parent[j][i-1]
            if half is not None:
                parent[j][i] = parent[half][i-1]


    M = int(input())
    #'''
    ans = []
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        ans.append(query(a, b)+1)

    print('\n'.join(map(str, ans)))

    #'''
    #print(query(0, 6))


def DP(i, j):
    if j == 0:
        return parent[i][j]
    if parent[i][j] is not None:
        return parent[i][j]

    halfParent = DP(i, j-1)
    if halfParent is not None:
        halfParentOfHalfParent = DP(halfParent, j-1)
        parent[i][j] = halfParentOfHalfParent
        return halfParentOfHalfParent
    return None


def query(a, b):
    if a == b:
        return a

    if a is None or b is None:
        assert False
    da = depth[a]
    db = depth[b]

    if da == db:
        for i in range(lN-1, -1, -1):
            pa = parent[a][i]
            pb = parent[b][i]

            if pa != pb:
                return query(pa, pb)
        return parent[a][0]

    if da < db:
        a, b = b, a
        da, db = db, da

    for i in range(lN-1, -1, -1):
        pa = parent[a][i]

        if pa is not None and depth[pa] >= db:
            return query(pa, b)

    return a


def query3(a, b):
    if a == b:
        return a
    da = depth[a]
    db = depth[b]

    if da == db:
        for i in range(lN-1, -1, -1):
            pa = parent[a][i]
            pb = parent[b][i]
            if pa != pb:

                return query(pa, pb)
        return parent[a][0]

    # a must be always deeper
    if da < db:
        a, b = b, a
        da, db = db, da

    for i in range(lN-1, -1, -1):
        dpa = da - 2 ** i
        if dpa >= db:
            return query(parent[a][i], b)
    return 0


def dfs(node, d):
    for i in g[node]:
        if not visited[i]:
            visited[i] = True
            parent[i][0] = node
            depth[i] = d + 1
            dfs(i, d + 1)


def query2(a, b):
    if a == b:
        return a

    da = depth[a]
    db = depth[b]

    if da < db:
        a, b = b, a
        da, db = db, da

    while depth[a] != db:
        a = parent[a][0]

    while a != b:
        a = parent[a][0]
        b = parent[b][0]

    return a


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
