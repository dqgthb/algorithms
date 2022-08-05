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

    global T, F, nameSet, nameToId, P, S
    T = int(input())
    for _ in range(T):

        F = int(input())

        nameSet = set()
        nameToId = {}
        P = []
        S = []
        idGen = 0

        for _ in range(F):

            name1, name2 = input().split()

            for name in (name1, name2):
                if name not in nameSet:
                    nameSet.add(name)
                    nameToId[name] = idGen
                    P.append(idGen)
                    S.append(1)
                    idGen += 1


            id1 = nameToId[name1]
            id2 = nameToId[name2]
            union(id1, id2)
            print(size(id1))




    # ######## INPUT AREA END ############


def find(x):
    if x != P[x]:
        P[x] = find(P[x])
    return P[x]


def union(x, y):
    fx = find(x)
    fy = find(y)

    if fx == fy:
        return
    elif fy < fx:
        fx, fy = fy, fx
    P[fy] = fx
    S[fx] += S[fy]

def size(x):
    return S[find(x)]


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