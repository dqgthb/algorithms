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

    global t, n, s, won
    t = int(input())
    for _ in range(t):
        n = int(input())
        won = [False] * n
        s = [int(i) for i in input().strip()]
        num2 = s.count(2)
        if 1 <= num2 <= 2:
            print("NO")
        else:
            print("YES")
            solve()

    # ######## INPUT AREA END ############
    # ####################################


def solve():
    mat = Mat(n, n, 'Z')
    for i in range(n):
        mat[i][i] = 'X'

    for i in range(n):
        p1 = s[i]
        for j in range(i+1, n):
            p2 = s[j]

            if p1 == 1 or p2 == 1:
                mat[i][j] = '='
                mat[j][i] = '='
            else:
                if not won[i]:
                    won[i] = True
                    mat[i][j] = '+'
                    mat[j][i] = '-'
                else:
                    won[j] = True
                    mat[i][j] = '-'
                    mat[j][i] = '+'




    pmat(mat)



def pmat(mat):
    for line in mat:
        print(''.join(map(str, line)))


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
