# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
import itertools
#from itertools import product
#import collections
from collections import deque, Counter, defaultdict as dd
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

    global tmp, tMat, nMat
    tmp = [0] * 9
    tMat = [[None] * 3 for _ in range(3)]
    nMat = [[None] * 3 for _ in range(3)]
    mat = [list(input().split()) for _ in range(3)]
    destination = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    desE = encode(destination)

    # ######## INPUT AREA END ############


    dq = deque()
    vis = set()
    matE = encode(mat)
    if matE == desE:
        print(0)
        return

    for i in range(9):
        if matE[i] == '0':
            dq.append((matE, i, 0))
    vis.add(matE)

    while dq:
        m, zeroPos, cnt = dq.popleft()

        for nmE, nzero in nextStep(m, zeroPos):
            if nmE == desE:
                print(cnt+1)
                return
            if not nmE in vis:
                vis.add(nmE)
                dq.append((nmE, nzero, cnt+1))
    print(-1)


def encode(mat):
    idx = 0
    for i in range(3):
        for j in range(3):
            tmp[idx] = str(mat[i][j])
            idx += 1
    return ''.join(tmp)


def decode(str_):
    idx = 0
    for i in range(3):
        for j in range(3):
            tMat[i][j] = str_[idx]
            idx += 1


dir = ((-1, 0), (1, 0), (0, -1), (0, 1))


def nextStep(str_, zeroPos):
    decode(str_)
    i, j = divmod(zeroPos, 3)

    for n in range(4):
        di, dj = dir[n]
        ni, nj = i + di, j + dj

        if 0 <= ni < 3 and 0 <= nj < 3:
            for a in range(3):
                for b in range(3):
                    nMat[a][b] = tMat[a][b]
            nMat[i][j] = tMat[ni][nj]
            nMat[ni][nj] = '0'
            yield encode(nMat), 3 * ni + nj




'''
def nextStep(mat):
    loc = None
    for i in range(3):
        for j in range(3):
            if mat[i][j] == '0':
                loc = (i, j)

    i, j = loc

    steps = []
    for n in range(4):
        di, dj = dir[n]
        ni, nj = i + di, j + dj

        if 0 <= ni < 3 and 0 <= nj < 3:
            nMat = [l[:] for l in mat]
            nMat[i][j] = mat[ni][nj]
            nMat[ni][nj] = '0'
            steps.append(nMat)
    return steps
'''


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