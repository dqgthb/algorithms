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
from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    T = int(input())
    n = int(input())
    A = [int(i) for i in input().split()]
    m = int(input())
    B = [int(i) for i in input().split()]

    # ######## INPUT AREA END ############

    pA = []
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += A[j]
            pA.append(sum_)

    pB = []
    for i in range(m):
        sum_ = 0
        for j in range(i, m):
            sum_ += B[j]
            pB.append(sum_)

    pA.sort()
    pB.sort()
    lpa = len(pA)
    lpb = len(pB)

    left = 0
    right = m-1

    cnt = 0
    print(pA)
    print(pB)
    while left < lpa and 0 <= right:
        a = pA[left]
        b = pB[right]
        c = a + b
        print(a, b, c)

        if c > T:
            right -= 1
        elif c < T:
            left += 1
        else:
            bCount = 1
            aCount = 1

            while right > 0 and pB[right-1] == b:
                bCount += 1
                right -= 1

            while left < m-1 and pA[left+1] == a:
                aCount += 1
                left += 1

            print(aCount, bCount)
            cnt += aCount * bCount
            left += 1

    print(cnt)


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