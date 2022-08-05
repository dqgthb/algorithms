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
    sys.setrecursionlimit(10**6+500)
    # ####################################
    # ######## INPUT AREA BEGIN ##########

    global N, G, dp
    N = int(input())
    G = [[] for _ in range(N)]
    dp = [[None, None] for _ in range(N)]
    for _ in range(N-1):
        u,v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)


    # ######## INPUT AREA END ############
    # ####################################

    i = 0
    g = createTreeWithRoot(i)
    del G
    c1 = solve(i, True, g)
    c2 = solve(i, False, g)
    ans = min(c1, c2)
    print(ans)


def createTreeWithRoot(root):
    g = [[] for _ in range(N)]
    visited = [False] * N

    dq = deque([root])
    visited[root] = True

    while dq:
        node = dq.popleft()
        for child in G[node]:
            if not visited[child]:
                visited[child] = True
                g[node].append(child)
                dq.append(child)
    return g


def solve(node, iAmEarlyAdaptor, graph):
    if dp[node][iAmEarlyAdaptor] is not None:
        return dp[node][iAmEarlyAdaptor]

    sum_ = 0
    if iAmEarlyAdaptor:
        sum_ = 1
        for child in graph[node]:
            sum_ += min(solve(child, True, graph), solve(child, False, graph))
    else:
        sum_ = 0
        for child in graph[node]:
            sum_ += solve(child, True, graph)
    dp[node][iAmEarlyAdaptor] = sum_
    return sum_


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
