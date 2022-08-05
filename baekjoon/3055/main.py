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

    global R, C, m, hedgehogExist, escapeSuccess
    R, C = map(int, input().split())
    m = [list(input().strip()) for _ in range(R)]

    escapeSuccess = False
    days = 0
    while True:
        hedgehogExist = False
        days += 1
        m = hedgehogUpdate(m)
        if escapeSuccess:
            print(days)
            return
        if not hedgehogExist:
            print("KAKTUS")
            return
        m = waterUpdate(m)


d = ((-1, 0), (1, 0), (0, 1), (0, -1))
def hedgehogUpdate(m):
    global hedgehogExist, escapeSuccess
    nm = [i[:] for i in m]

    for i in range(R):
        for j in range(C):
            if m[i][j] == 'S':
                hedgehogExist = True
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        if m[ni][nj] == 'D':
                            escapeSuccess = True
                            return nm
                        elif m[ni][nj] == '.':
                            nm[ni][nj] = 'S'
    return nm


def waterUpdate(m):
    nm = [i[:] for i in m]
    for i in range(R):
        for j in range(C):
            if m[i][j] == '*':
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        if m[ni][nj] in '.S':
                            nm[ni][nj] = '*'
    return nm


    # ######## INPUT AREA END ############


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