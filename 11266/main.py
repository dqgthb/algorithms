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
    sys.setrecursionlimit(10**5 + 1000)
    # ######## INPUT AREA BEGIN ##########

    global V, E, G, time, disc, isCut
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]

    time = 0
    disc = [-1] * V
    isCut = [False] * V

    for _ in range(E):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    # ######## INPUT AREA END ############

    tarjan()

    cutVertices = []
    for i, e in enu(isCut):
        if e:
            cutVertices.append(i)
    print(len(cutVertices))
    print(' '.join(map(str, (i+1 for i in cutVertices))))



def tarjan():
    global root
    for i in range(V):
        if disc[i] == -1:
            root = i
            dfs(i)


def dfs(node):
    global time
    disc[node] = time
    ret = time
    time += 1
    childCount = 0

    for v in G[node]:

        if disc[v] == -1:
            childCount += 1
            sub = dfs(v)
            if node != root and disc[node] <= sub:
                isCut[node] = True
            ret = min(ret, sub)
        else:
            ret = min(ret, disc[v])


    if node == root: # root node
        if childCount > 1:
            isCut[node] = True
    return ret


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