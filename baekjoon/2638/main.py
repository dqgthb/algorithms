# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
from collections import deque
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

    global D, N, M, mat
    D = ((-1, 0), (1, 0), (0, 1), (0, -1))
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # ######## INPUT AREA END ############


    airDFS(0, 0)
    time = 0
    cheeseRemains = True
    while cheeseRemains:
        cheeseRemains = False
        for i in range(N):
            for j in range(M):
                if mat[i][j] == 1:
                    cheeseRemains = True
                    cnt = 0
                    for di, dj in D:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < M:
                            if mat[ni][nj] == 2:
                                cnt += 1

                    if cnt > 1:
                        mat[i][j] = 3

        if not cheeseRemains:
            break

        time += 1

        for i in range(N):
            for j in range(M):
                if mat[i][j] == 3:
                    airDFS(i, j)
    print(time)



def airDFS(i, j):
    mat[i][j] = 2
    dq = [(i, j)]
    while dq:
        i, j = dq.pop()

        for di, dj in D:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if mat[ni][nj] == 0:
                    mat[ni][nj] = 2
                    dq.append((ni, nj))






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