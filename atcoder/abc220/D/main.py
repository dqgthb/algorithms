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

    N = int(input())
    A = [int(i) for i in input().split()]
    MOD = 998244353

    # ######## INPUT AREA END ############

    freq = [0] * 10
    new = [0] * 10
    freq[A[0]] = 1
    for i in range(1, N):
        for k in range(10):
            new[k] = 0

        ai = A[i]
        for j in range(10):
            val = freq[j]
            f = (ai + j) % 10
            g = (ai * j) % 10
            new[f] += val
            new[f] %= MOD
            new[g] += val
            new[g] %= MOD
        for k in range(10):
            freq[k] = new[k]
    parr(freq)









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