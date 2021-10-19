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
    global p, s, N
    N = int(input())
    s =[(0, 0, 0, 0)]
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        s.append((x1, y1, x2, y2))
    s.sort()
    parr(s)

    # ######## INPUT AREA END ############

    p = [i for i in range(N+1)]
    for i in range(N+1):
        si = s[i]
        for j in range(i+1, N+1):
            sj = s[j]
            if sj[0] > si[2]:
                break
            if find(i) == find(j):
                continue
            if check(*si, *sj):
                union(i, j)

    for i in range(N+1):
        find(i)

    exist = [False] * (N+1)
    cnt = 0
    print(p)
    for i in p:
        if exist[i] == False:
            exist[i] = True
            cnt += 1
    print(cnt-1)

    print(check(*s[3], *s[5]))


def check(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):

    for k in range(2):
        if k == 1:
            ax1, ax2, ay1, ay2, bx1, bx2, by1, by2 =\
                bx1, bx2, by1, by2, ax1, ax2, ay1, ay2
        ax = (ax1, ax2)
        ay = (ay1, ay2)
        inCount = 0
        bIn = False
        print(bx1, bx2, by1, by2)
        for i in range(2):
            for j in range(2):
                print(ax[i], ay[j])
                if (bx1 < ax[i] < bx2) and (by1 < ay[j] < by2):
                    inCount += 1
                if (bx1 <= ax[i] <= bx2) and (by1 <= ay[j] <= by2):
                    bIn = True
        if inCount == 4:
            return False
        if bIn:
            return True
        if ax1 <= bx1 and bx2 <= ax2 and by1 <= ay1 and ay2 <= by2:
            return True

    return False


def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]


def union(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        return

    p[py] = p[px] = px if px < py else py


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