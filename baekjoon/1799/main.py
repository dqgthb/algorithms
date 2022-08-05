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

    global N, mat, maxCount, LB, LW
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # ######## INPUT AREA END ############

    global diaLeft, diaRight, blackOnes, whiteOnes, cnt
    blackIfTrue = True
    diaLeft = [False] * (N * 2 - 1)
    diaRight = [False] * (N * 2 - 1)
    blackOnes = []
    whiteOnes = []
    isNEven = N % 2 == 0

    for i in range(N):
        if isNEven:
            blackIfTrue = not blackIfTrue
        for j in range(N):
            if mat[i][j] == 1:
                if blackIfTrue:
                    blackOnes.append((i, j))
                else:
                    whiteOnes.append((i, j))
            blackIfTrue = not blackIfTrue

    LB = len(blackOnes)
    LW = len(whiteOnes)

    ans = 0
    cnt = 0
    maxCount = 0
    dfsBlack(0)
    ans += maxCount

    maxCount = 0
    dfsWhite(0)
    ans += maxCount
    print(ans)


def dfsBlack(i):
    global maxCount, cnt
    if i == LB:
        maxCount = max(maxCount, cnt)
        return

    x, y = blackOnes[i]
    l = N + y - x - 1
    r = x + y
    if not diaLeft[l] and not diaRight[r]:
        mat[x][y] = 2
        diaLeft[l] = diaRight[r] = True
        cnt += 1
        dfsBlack(i+1)
        cnt -= 1
        mat[x][y] = 1
        diaLeft[l] = diaRight[r] = False
    dfsBlack(i+1)


def dfsWhite(i):
    global maxCount, cnt
    if i == LW:
        maxCount = max(maxCount, cnt)
        return

    x, y = whiteOnes[i]
    l = N + y - x - 1
    r = x + y
    if not diaLeft[l] and not diaRight[r]:
        mat[x][y] = 2
        diaLeft[l] = diaRight[r] = True
        cnt += 1
        dfsWhite(i+1)
        cnt -= 1
        mat[x][y] = 1
        diaLeft[l] = diaRight[r] = False
    dfsWhite(i+1)



# TEMPLATE ###############################

enu = enumerate


def For(*args):
    return product(*map(range, args))


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