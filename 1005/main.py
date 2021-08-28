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

    global T, N, K, times, G, numParens, target
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        times = [int(i) for i in input().split()]
        G = [[] for _ in range(N)]
        numParens = [0 for _ in range(N)]

        for _ in range(K):
            from_, to = map(int, input().split())
            from_ -= 1
            to -= 1
            G[from_].append(to)
            numParens[to] += 1
        target = int(input())-1
        solve()


    # ######## INPUT AREA END ############
    # ####################################

def solve():
    q = deque()
    ans = []
    time = [0 for _ in range(N)]
    for i, e in enu(numParens):
        if e == 0:
            q.append((i, 0))

    while q:
        building, tier = q.popleft()
        ans.append(building)
        time[tier] = max(time[tier], times[building])
        if building == target:
            print(sum(time[:tier+1]))
            return
        for nextBuilding in G[building]:
            numParens[nextBuilding] -= 1
            if numParens[nextBuilding] == 0:
                q.append((nextBuilding, tier + 1))







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
