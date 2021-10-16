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
from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, A, T
    N = int(input())
    A = [int(i) for i in input().split()]
    N = len(A)
    Asorted = list(sorted(A))
    convert = {Asorted[i]:i for i in range(N)}
    print(convert)

    # ######## INPUT AREA END ############

    for i in range(N):
        A[i] = convert[A[i]]
    print(A)

    F = [0] * N
    T = [0] * (2**(ceil(log2(N))+1))
    #segInit(0, N-1, 1)
    print(T)

    cnt = 0

    for i in A:
        numsLarger = segQuery(0, N-1, i+1, N-1, 1)
        cnt += numsLarger
        F[i] += 1
        segUpdate(0, N-1, i, F[i], 1)
    print(cnt)



def segInit(s, e, idx, arr):
    if s == e:
        T[idx] = arr[s]
        return T[idx]

    mid = (s + e)//2
    T[idx] = segInit(s, mid, idx * 2) + segInit(mid+1, e, idx * 2 + 1)
    return T[idx]


def segQuery(s, e, left, right, idx):
    if e < left or right < s:
        return 0

    if left <= s and e <= right:
        return T[idx]

    mid = (s + e) // 2
    return segQuery(s, mid, left, right, idx * 2) + segQuery(mid+1, e, left, right, idx * 2 + 1)


def segUpdate(s, e, i, v, idx):
    if i < s or e < i:
        return T[idx]

    if s == e == i:
        T[idx] = v
        return v

    mid = (s + e) // 2
    T[idx] = segUpdate(s, mid, i, v, idx * 2) + segUpdate(mid+1, e, i, v, idx * 2 + 1)
    return T[idx]








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