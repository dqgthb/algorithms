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


MOD = 10 ** 9 + 7
def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########
    global N, A, M, T, L
    N = int(input())
    A = [int(i) for i in input().split()]
    M = int(input())
    h = ceil(log2(N))
    s = (1 << (h+1))
    T = [0] * s
    L = [[1,0] for _ in range(s)]

    segInit(0, N-1, 1)

    for _ in range(M):
        a, *q = [int(i) % MOD for i in input().split()]

        #print(T)
        #for i in range(N):
        #    ans = query(0, N-1, 1, i, i)
        #    print(ans, end=' ')
        #print()


        if a == 4:
            b, c = q
            b -= 1
            c -= 1
            ans = query(0, N-1, 1, b, c)
            print(ans)
        else:
            b, c, d = q
            b -= 1
            c -= 1

            if a == 1:
                addRange(0, N-1, 1, b, c, d)
            elif a == 2:
                mulRange(0, N-1, 1, b, c, d)
            else:
                updateRange(0, N-1, 1, b, c, d)


    # ######## INPUT AREA END ############


def segInit(s, e, i):
    if s == e:
        T[i] = A[s] % MOD
        return T[i]

    m = (s + e) // 2
    T[i] = segInit(s, m, 2*i) + segInit(m+1, e, 2*i+1)
    T[i] %= MOD
    return T[i]


def lazyUpdate(s, e, i):
    if L[i] == [1, 0]: return
    m, a = L[i]
    m %= MOD
    a %= MOD
    T[i] = (m * T[i]) % MOD
    T[i] += (e - s + 1) * a
    T[i] %= MOD
    if s != e:
        for j in range(2):
            child = i*2 + j
            m2, a2 = L[child]
            L[child][0] *= m
            L[child][1] = (a2 * m + a) % MOD

    L[i] = [1, 0]


def addRange(s, e, i, l, r, v):
    lazyUpdate(s, e, i)
    if s > r or e < l:
        return

    if l <= s and e <= r:
        L[i][1] += v
        L[i][1] %= MOD
        lazyUpdate(s, e, i)
        return

    m = (s + e) // 2
    addRange(s, m, 2*i, l, r, v)
    addRange(m+1, e, 2*i+1, l, r, v)
    T[i] = T[2*i] + T[2*i+1]
    T[i] %= MOD


def updateRange(s, e, i, l, r, v):
    lazyUpdate(s, e, i)
    if s > r or e < l:
        return

    if l <= s and e <= r:
        L[i][0] = 0
        L[i][1] = v
        lazyUpdate(s, e, i)
        return

    m = (s + e) // 2
    updateRange(s, m, i*2, l, r, v)
    updateRange(m+1, e, i*2+1, l, r, v)
    T[i] = T[2*i] + T[2*i+1]
    T[i] %= MOD


def query(s, e, i, l, r):
    lazyUpdate(s, e, i)

    if s > r or e < l:
        return 0

    if l <= s and e <= r:
        return T[i] % MOD

    m = (s + e)//2
    ret = query(s, m, 2*i, l, r) + query(m+1, e, 2*i+1, l, r)
    return ret % MOD


def mulRange(s, e, i, l, r, v):
    lazyUpdate(s, e, i)
    if s > r or e < l:
        return

    if l <= s and e <= r:
        L[i][0] *= v
        L[i][0] %= MOD
        lazyUpdate(s, e, i)
        return

    m = (s + e) // 2
    mulRange(s, m, 2*i, l, r, v)
    mulRange(m+1, e, 2*i+1, l, r, v)
    T[i] = T[2*i] + T[2*i+1]
    T[i] %= MOD


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