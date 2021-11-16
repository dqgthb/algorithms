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
    global N, E, G, u, v, S, T
    N, E = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, c))
        G[b].append((a, c))
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    # ######## INPUT AREA END ############

    s = 0
    t = N-1
    ds = dijkstra(s)
    du = dijkstra(u)
    dv = dijkstra(v)

    c1 = ds[u] + du[v] + dv[t]
    c2 = ds[v] + dv[u] + du[t]

    ans = min(c1, c2)
    if ans >= 10 ** 9:
        print(-1)
    else:
        print(ans)




def dijkstra(s):
    dist = [10**9] * N
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        dsx, x = heappop(pq)
        if dsx > dist[x]:
            continue

        for y, dxy in G[x]:
            dsy = dsx + dxy

            if dsy < dist[y]:
                dist[y] = dsy
                heappush(pq, (dsy, y))
    return dist





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