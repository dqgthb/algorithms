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
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    # floyd-warshall can also solve it but it takes too long time.

    global N, G, P, D, DIST, vis, LIM
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b, v = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, v))
        G[b].append((a, v))


    LIM = 17


    # P[a][k] is the 2**kth parent node of a.
    P = [[None for _ in range(LIM)] for _ in range(N)]
    vis = [False for _ in range(N)]
    # DIST[a][k] is the distance between a and the 2**kth parent.
    DIST = [[None for _ in range(LIM)] for _ in range(N)]
    D = [None] * N
    D[0] = 0
    vis[0] = True

    # DFS. Form a tree and log parents
    stack = [0]
    while stack:
        v = stack.pop()
        d = D[v]
        for w, dist in G[v]:
            if not vis[w]:
                vis[w] = True
                P[w][0] = v
                DIST[w][0] = dist

                for i in range(15):
                    p = P[w][i]
                    if p is None:
                        break

                    pp = P[p][i]
                    if P[p][i] is None:
                        break

                    P[w][i+1] = pp
                    DIST[w][i+1] = DIST[w][i] + DIST[p][i]
                D[w] = d + 1
                stack.append(w)


    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        print(rca(a, b))

    # ######## INPUT AREA END ############


def rca(a, b):
    if D[a] < D[b]:
        a, b = b, a

    aDist = 0
    bDist = 0

    for k in range(LIM-1, -1, -1):
        p = P[a][k]
        if p is None: continue
        if D[p] < D[b]: continue
        else:
            aDist += DIST[a][k]
            a = p
            if D[a] == D[b]:
                break


    if a != b:
        for k in range(LIM-1, -1, -1):
            pa = P[a][k]
            pb = P[b][k]
            if pa is None:
                continue
            if pa != pb:
                aDist += DIST[a][k]
                a = pa
                bDist += DIST[b][k]
                b = pb
        aDist += DIST[a][k]
        bDist += DIST[b][k]

    return aDist + bDist



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