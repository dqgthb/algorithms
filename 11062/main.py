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
    global T, N, A, D

    T = int(input())
    for _ in range(T):
        N = int(input())
        A = [int(i) for i in input().split()]
        D = nDim(N, N, 2)
        print(solve(0, N-1, True))



    # ######## INPUT AREA END ############


def solve(s, e, flag):
    if D[s][e][flag]:
        return D[s][e][flag]

    if flag:
        if s == e:
            return A[s]
        c1 = A[s] + solve(s+1, e, not flag)
        c2 = A[e] + solve(s, e-1, not flag)
        #print(c1, c2, flag, "select", max(c1, c2))
        D[s][e][flag] = max(c1, c2)
        return max(c1, c2)

    else:
        if s == e:
            return 0
        c1 = solve(s+1, e, not flag)
        c2 = solve(s, e-1, not flag)
        #print(c1, c2, flag)
        D[s][e][flag] = min(c1, c2)
        return min(c1, c2)


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