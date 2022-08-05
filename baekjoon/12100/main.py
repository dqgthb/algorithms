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

    global N, mat, merged, max_, command, cnt
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    merged = Mat(N, N, default=False)
    max_ = -1
    command = []
    cnt = 0

    # ######## INPUT AREA END ############
    # ####################################

    dfs(5)
    print(max_)


def dfs(step = 5):
    global mat, cnt
    global max_
    if step == 0:
        print(command)
        parr(mat)
        max_ = max(max_, findMax())
        return

    copy = [arr[:] for arr in mat]

    moveUp()
    command.append("up")
    dfs(step - 1)
    for i in range(N):
        for j in range(N):
            mat[i][j] = copy[i][j]
    command.pop()

    moveLeft()
    command.append("left")
    dfs(step - 1)
    for i in range(N):
        for j in range(N):
            mat[i][j] = copy[i][j]
    command.pop()

    moveDown()
    command.append("down")
    dfs(step - 1)
    command.pop()
    for i in range(N):
        for j in range(N):
            mat[i][j] = copy[i][j]

    moveRight()
    command.append("right")
    dfs(step - 1)
    command.pop()



def findMax():
    max_ = -1
    for i in range(N):
        for j in range(N):
            max_ = max(max_, mat[i][j])
    return max_


def clearMerged():
    for i in range(N):
        for j in range(N):
            merged[i][j] = False


def moveUp():
    for c in range(N):
        for r in range(N):
            while r > 0:
                if mat[r-1][c] == 0:
                    mat[r-1][c] = mat[r][c]
                    mat[r][c] = 0
                    r -= 1
                elif mat[r-1][c] == mat[r][c] and not merged[r-1][c]:
                    mat[r-1][c] *= 2
                    mat[r][c] = 0
                    merged[r-1][c] = True
                else:
                    break
    clearMerged()


def moveDown():
    for c in range(N):
        for r in range(N-1, -1, -1):
            while r < N-1:
                if mat[r+1][c] == 0:
                    mat[r+1][c] = mat[r][c]
                    mat[r][c] = 0
                    r += 1
                elif mat[r+1][c] == mat[r][c] and not merged[r+1][c]:
                    mat[r+1][c] *= 2
                    mat[r][c] = 0
                    merged[r+1][c] = True
                else:
                    break
    clearMerged()


def moveLeft():
    for r in range(N):
        for c in range(N):
            while c > 0:
                if mat[r][c-1] == 0:
                    mat[r][c-1] = mat[r][c]
                    mat[r][c] = 0
                    c -= 1
                elif mat[r][c-1] == mat[r][c] and not merged[r][c-1]:
                    mat[r][c-1] *= 2
                    mat[r][c] = 0
                    merged[r][c-1] = True
                else:
                    break
    clearMerged()


def moveRight():
    for r in range(N):
        for c in range(N-1, -1, -1):
            while c < N-1:
                if mat[r][c+1] == 0:
                    mat[r][c+1] = mat[r][c]
                    mat[r][c] = 0
                    c += 1
                elif mat[r][c+1] == mat[r][c] and not merged[r][c+1]:
                    mat[r][c+1] *= 2
                    mat[r][c] = 0
                    merged[r][c+1] = True
                else:
                    break
    clearMerged()









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
