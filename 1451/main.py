# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
import itertools
#from itertools import product
#import collections
#from collections import deque, Counter, defaultdict as dd
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

    global N, M, MAT, CUM
    N, M = map(int, input().split())

    MAT = [list(map(int, input().strip())) for _ in range(N)]
    CUM = Mat(N, M)

    # ######## INPUT AREA END ############

    # build CUM
    CUM[0][0] = MAT[0][0]
    for i in range(1, M):
        CUM[0][i] = CUM[0][i-1] + MAT[0][i]

    for i in range(1, N):
        CUM[i][0] = CUM[i-1][0] + MAT[i][0]

    for i in range(1, N):
        for j in range(1, N):
            CUM[i][j] = CUM[i-1][j] + CUM[i][j-1] - CUM[i-1][j-1] + MAT[i][j]

    for i in range(0, N):
        for j in range(0, M):
            for k in range(i, N):
                for l in range(j, M):
                    parr(MAT)
                    print(i, j, k, l, query(i, j, k, l))

    # divide horizontally

    # divide vertically


def query(ai, aj, bi, bj):
    ret = CUM[bi][bj]
    if ai == 0:
        if aj == 0:
            return ret
        else:
            return ret - CUM[bi][aj-1]
    else:
        if aj == 0:
            return ret - CUM[ai-1][bj]
        else:
            return ret - CUM[ai-1][bj] - CUM[bi][aj-1] + CUM[ai-1][aj-1]




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