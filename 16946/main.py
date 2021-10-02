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


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def main(f=None):
    init(f)
    #sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, M, mat, nums
    N, M = map(int, input().split())
    mat = [[int(i) for i in input().strip()] for _ in range(N)]

    # ######## INPUT AREA END ############

    nums = []
    groupNo = 2
    wallPositions = []
    for i in range(N):
        for j in range(M):
            '''
            if mat[i][j] == 0:
                cnt = 0
                stack = deque([(i, j)])
                mat[i][j] = groupNo
                while stack:
                    i, j = stack.popleft()
                    cnt += 1
                    for x, y in zip(dx, dy):
                        ni = i + x
                        nj = j + y
                        if 0 <= ni < N and 0 <= nj < M:
                            if mat[ni][nj] == 0:
                                mat[ni][nj] = groupNo
                                stack.append((ni, nj))
                groupNo += 1
                nums.append(cnt)

            '''
            if mat[i][j] == 1:
                wallPositions.append((i, j))

    parr(mat)
    print(wallPositions)

    cpy = Mat(N, M, 0)
    print(wallPositions)
    for i, j in wallPositions:
        s = set()
        sum_ = 1
        for x, y in zip(dx, dy):
            ni = i + x
            nj = j + y
            if 0 <= ni < N and 0 <= nj < M:
                grp = mat[ni][nj]
                if grp != 1 and not grp in s:
                    s.add(grp)
                    sum_ += nums[grp - 2]
        cpy[i][j] = sum_ % 10

    for line in cpy:
        print(''.join(map(str, line)))


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