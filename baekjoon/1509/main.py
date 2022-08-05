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

    S = input().strip()
    N = len(S)
    DP = [i+1 for i in range(N)]

    PAL = [[False for _ in range(N)] for _ in range(N)]

    # ######## INPUT AREA END ############

    for i in range(N-1):
        PAL[i][i+1] = S[i] == S[i+1]
        PAL[i][i] = True
    PAL[N-1][N-1] = True


    for l in range(2, N):
        for i in range(N-l):
            j = i + l
            PAL[i][j] = S[i] == S[j] and PAL[i+1][j-1]


    for i in range(1, N):
        if PAL[0][i]:
            DP[i] = 1
            continue
        DP[i] = DP[i-1] + 1
        for j in range(1, i):
            if PAL[j][i]:
                DP[i] = min(DP[i], DP[j-1] + 1)
    print(DP[N-1])








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