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


dir = ((-1, 0), (1, 0), (0, 1), (0, -1))
def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, mat, cpy
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    cpy = Mat(N, N)

    # ######## INPUT AREA END ############

    cnt = 2
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                mat[i][j] = cnt
                dq = deque()
                dq.append((i, j))
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in dir:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < N and 0 <= ny < N:
                            if mat[nx][ny] == 1:
                                mat[nx][ny] = cnt
                                dq.append((nx, ny))
                cnt += 1

    global min_
    min_ = 10**9

    for i in range(2, cnt):
        min_ = min(min_, solve(i)-1)
    print(min_)



def solve(n):
    dq = deque()

    for i in range(N):
        for j in range(N):
            if mat[i][j] == n:
                cpy[i][j] = 1
                dq.append((i, j))
            else:
                cpy[i][j] = 0

    while dq:
        x, y = dq.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if cpy[nx][ny] == 0:
                if mat[nx][ny] != 0:
                    return cpy[x][y]
                cpy[nx][ny] = cpy[x][y] + 1
                dq.append((nx, ny))

    parr(cpy)
    print()



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