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

    global N, A, B, Ac, Bc, T, C
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    T = [None] * N

    # ######## INPUT AREA END ############

    convert = {B[i]:i for i in range(N)}
    Ac = [convert[i] for i in A]
    Bc = [i for i in range(N)]
    C = 0

    print(A)
    print(B)

    print(Ac)
    print(Bc)

    mergeSort(0, N-1)
    print(Ac)


def mergeSort(s, e):
    global C
    if s == e:
        return

    mid = (s + e) // 2
    mergeSort(s, mid)
    mergeSort(mid+1, e)

    cnt = merge(s, e)
    C += cnt



def merge(s, e):
    mid = (s + e) // 2

    idx = s
    l = s
    r = mid + 1
    state = 1
    cnt = 0

    while state == 1:
        if Ac[l] <= Ac[r]:
            T[idx] = Ac[l]
            idx += 1
            l += 1
            if l > mid:
                state = 2

        else:
            T[idx] = Ac[r]
            idx += 1
            r += 1
            cnt += 1
            if r > e:
                state = 3

    if state == 2:
        while r <= e:
            T[idx] = Ac[r]
            idx += 1
            r += 1
            cnt += 1

    else:
        while l <= mid:
            T[idx] = Ac[l]
            idx += 1
            l += 1

    for i in range(s, e+1):
        Ac[i] = T[i]
    return cnt










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