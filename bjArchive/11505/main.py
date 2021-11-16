# CP template Version 1.006
import os
import sys
import itertools
import collections
import string
# not for python < 3.9
# from functools import cmp_to_key, reduce, partial, cache
from functools import cmp_to_key, reduce, partial
from itertools import product
from collections import deque, Counter, defaultdict as dd
from math import log, log2, ceil, floor, gcd, sqrt
import math
from heapq import heappush, heappop
from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ####################################
    # ######## INPUT AREA BEGIN ##########

    global N, M, K, arr, t, MOD
    MOD = 10 ** 9 + 7
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    t = [None] * 2 * 2**ceil(log2(N))
    buildT(0, N-1, 1)
    answers = []
    for _ in range(M + K):
        a, b, c = map(lambda x: int(x) -1, input().split())
        if a == 0:
            c += 1
            update(0, N-1, 1, b, c)
            arr[b] = c
        else:
            ans = query(0, N-1, 1, b, c)
            answers.append(ans)
    print('\n'.join(map(str, answers)))


    # ######## INPUT AREA END ############
    # ####################################


def buildT(left, right, idx):
    if left == right:
        t[idx] = arr[left]
        return t[idx]
    mid = (left + right) // 2
    t[idx] = buildT(left, mid, idx * 2) * buildT(mid + 1, right, idx * 2 + 1) % MOD
    return t[idx]


def update(start, end, idx, b, changed):
    if start == end:
        t[idx] = changed
        return t[idx]

    mid = (start + end) // 2
    if start <= b <= mid:
        res = update(start, mid, idx * 2, b, changed)
        t[idx] = res * t[idx * 2 + 1] % MOD
        return t[idx]
    else:
        res = update(mid+1, end, idx * 2+1, b, changed)
        t[idx] = res * t[idx * 2] % MOD
        return t[idx]


def query(start, end, idx, left, right):
    if right < start:
        return 1
    if end < left:
        return 1
    if left <= start and end <= right:
        return t[idx]

    mid = (start + end) // 2
    leftQuery = query(start, mid, idx * 2, left, right)
    rightQuery = query(mid+1, end, idx * 2 + 1, left, right)
    return leftQuery * rightQuery % MOD






# #############################################################################
# #############################################################################
# ############################## TEMPLATE AREA ################################
# #############################################################################
# #############################################################################

enu = enumerate


def argmax(arr):
    return max(enumerate(arr), key=lambda x: x[1])


def argmin(arr):
    return min(enumerate(arr), key=lambda x: x[1])


def For(*args):
    return itertools.product(*map(range, args))


def copy2d(mat):
    return [row[:] for row in mat]


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


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()
