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
from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, M, A, T, L
    N = int(input())
    A = [int(i) for i in input().split()]
    M = int(input())

    T = [None] * (1 << (ceil(log2(N)) + 1))
    L = [0] * (1 << (ceil(log2(N)) + 1))
    segInit(0, N-1, 1)

    for _ in range(M):
        a, *arr = map(int, input().split())

        if a == 1:
            b, c, d = arr
            if b > c:
                b, c = c, b
            rangeXor(0, N-1, 1, b, c, d)
        else:
            b, c = arr
            if b > c:
                b, c = c, b
            ans = queryXor(0, N-1, 1, b, c)
            print(ans)


    # ######## INPUT AREA END ############


def segInit(s, e, i) -> int:
    if s == e:
        T[i] = A[s]
        return T[i]

    mid = s + e >> 1
    T[i] = segInit(s, mid, i*2) ^ segInit(mid+1, e, i*2+1)
    return T[i]


def lazyUpdate(s, e, i):
    if L[i] != 0:
        T[i] ^= L[i] * ((e - s + 1) % 2)
        if s != e:
            L[i*2] ^= L[i]
            L[i*2+1] ^= L[i]
        L[i] = 0


def rangeXor(s, e, i, l, r, v) -> None:
    lazyUpdate(s, e, i)
    if r < s or e < l:
        return

    if l <= s and e <= r:
        #L[i] = v
        #lazyUpdate(s, e, i)

        T[i] ^= v * ((e - s + 1) % 2)
        if s != e:
            L[i*2] ^= v
            L[i*2+1] ^= v
        return

    m = s + e >> 1
    rangeXor(s, m, i*2, l, r, v)
    rangeXor(m+1, e, i*2+1, l, r, v)
    T[i] = T[i*2] ^ T[i*2+1]


def queryXor(s, e, i, l, r) -> int:
    lazyUpdate(s, e, i)

    if r < s or e < l:
        return 0

    if l <= s and e <= r:
        return T[i]

    m = s + e >> 1
    q1 = queryXor(s, m, i*2, l, r)
    q2 = queryXor(m+1, e, i*2+1, l, r)
    return q1 ^ q2


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