# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
import itertools
#from itertools import product
#import collections
from collections import deque, Counter, defaultdict as dd
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

    global N, M, K, mat, S, L
    N, M, K = map(int, input().split())
    mat = [list(input().strip()) for _ in range(N)]
    S = input().strip()
    L = len(S)

    # ######## INPUT AREA END ############

    dp = Mat(N, M, 0)

    dq = deque()
    for i in range(N):
        for j in range(M):
            if mat[i][j] == S[-1]:
                dp[i][j] = 1
                dq.append((i, j, L-1))


    cum = 0
    while dq:
        i, j, c = dq.popleft()
        if c == 0:
            cum += dp[i][j]
            continue

        for di, dj in dir:
            for k in range(1, K+1):
                ni, nj = i + k * di, j + k * dj
                if 0 <= ni < N and 0 <= nj < M:
                    if mat[ni][nj] == S[c-1]:
                        if dp[ni][nj] == 0:
                            dq.append((ni, nj, c-1))
                        dp[ni][nj] += dp[i][j]

    parr(dp)
    print(cum)


dir = ((-1, 0), (1, 0), (0, 1), (0, -1))


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