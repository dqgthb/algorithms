# CP template Version 1.006
#import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque, Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


input = sys.stdin.readline  # by default
def main(f=None):
    #init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, A, T, Ans
    N = int(input())
    A = [int(i) for i in input().split()]
    T = A[:]
    N = len(A)
    Ans = 0
    mergeSort(0, N-1)

    print(Ans)



    # ######## INPUT AREA END ############


def mergeSort(s, e):
    global Ans
    if s == e:
        return
    mid = (s + e) // 2
    mergeSort(s, mid)
    mergeSort(mid+1, e)
    Ans += merge(s, e)



def merge(s, e):
    mid = (s + e) // 2
    cnt = e - s + 1

    l = s
    r = mid + 1
    idx = s
    ans = 0

    state = 0
    # state:
    # l <= mid and r <= e: 0
    # l > mid and r <= e: 1
    # l <= mid and r > e: 2
    # l > mid and r > e: 3

    while True: # state == 0
        if A[l] <= A[r]:
            ans += r - mid - 1
            T[idx] = A[l]
            l += 1
            idx += 1
            if l > mid:
                state = 1
                break
        else:
            T[idx] = A[r]
            r += 1
            idx += 1
            if r > e:
                state = 2
                break

    if state == 1:
        while r <= e:
            T[idx] = A[r]
            r += 1
            idx += 1
    else:
        while l <= mid:
            ans += r - mid - 1
            T[idx] = A[l]
            l += 1
            idx += 1

    for i in range(s, e+1):
        A[i] = T[i]

    return ans


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