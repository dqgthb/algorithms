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

    global N, K, A, T
    while True:
        try:
            N, K = map(int, input().split())
        except:
            return
        A = [int(i) for i in input().split()]
        for i in range(N):
            a = A[i]
            if a > 0:
                A[i] = 1
            elif a < 0:
                A[i] = -1

        T = [None] * (4 * N)
        segInit(0, N-1, 1)

        ans = []

        for _ in range(K):
            a, b, c = input().split()
            b = int(b)
            c = int(c)

            if a == 'C':
                b -= 1
                if c > 0:
                    c = 1
                elif c < 0:
                    c = -1
                change(0, N-1, 1, b, c)
            else:
                b -= 1
                c -= 1
                res = product(0, N-1, 1, b, c)
                if res > 0:
                    ans.append("+")
                elif res == 0:
                    ans.append("0")
                else:
                    ans.append("-")
        print("".join(ans))

    # ######## INPUT AREA END ############


def segInit(s, e, i):
    if s == e:
        T[i] = A[s]
        return T[i]

    m = (s + e) // 2
    T[i] = segInit(s, m, i*2) * segInit(m+1, e, i*2+1)
    return T[i]


def change(s, e, i, idx, val):

    if idx < s or e < idx:
        return T[i]

    if s == e:
        T[i] = val
        return T[i]

    m = (s + e) // 2
    T[i] = change(s, m, i*2, idx, val) * change(m+1, e, i*2+1, idx, val)
    return T[i]


def product(s, e, i, l, r):

    if r < s or e < l:
        return 1

    if l <= s and e <= r:
        return T[i]

    m = (s + e) // 2
    return product(s, m, i*2, l, r) * product(m+1, e, i*2+1, l, r)


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