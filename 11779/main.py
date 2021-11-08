# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########
    global N, M
    N = int(input())
    M = int(input())
    G = [[] for _ in range(N)]

    for _ in range(M):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        G[x].append((y, z))

    s, t = map(int, input().split())
    s -= 1
    t -= 1

    D = [10**9] * N
    P = [-1] * N
    D[s] = 0
    pq = [(0, s)]

    while pq:
        d, i = heappop(pq)
        if D[i] < d:
            continue

        for j, dij in G[i]:
            dsj = d + dij
            if dsj < D[j]:
                D[j] = dsj
                P[j] = i
                pq.append((dsj, j))

    print(D[t])

    path = []
    curr = t
    while curr != -1:
        path.append(curr)
        curr = P[curr]
    print(len(path))
    print(' '.join(str(i+1) for i in reversed(path)))







    # ######## INPUT AREA END ############


# TEMPLATE ###############################


enu = enumerate


def For(*args):
    return itertools.product(*map(range, args))


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


def pr(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()