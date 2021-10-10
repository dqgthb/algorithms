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

    global S, dp
    S = [int(i) for i in input().strip()]
    dp = [0] * len(S)

    # ######## INPUT AREA END ############

    if S[0] == 0:
        print(0)
        return
    if len(S) == 1:
        print(1)
        return
    for i in range(1, len(S)):
        if S[i] == 0:
            if not 0 < S[i-1] < 3:
                print(0)
                return
    dp[0] = 1
    dp[1] = 1
    if S[0] == 1:
        dp[1] = 2
    elif S[0] == 2 and S[1] < 7:
        dp[1] = 2

    if S[1] == 0:
        dp[0] = 0
        dp[1] = 1

    for i in range(2, len(S)):
        dp[i] = dp[i-1]
        if S[i] == 0:
            dp[i] = dp[i-2]
            dp[i-1] = 0
            continue
        if S[i-1] == 1:
            dp[i] += dp[i-2]
        elif S[i-1] == 2 and S[i] < 7:
            dp[i] += dp[i-2]
        dp[i] %= 1000000

    #print(dp)
    print(dp[len(S) - 1])


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