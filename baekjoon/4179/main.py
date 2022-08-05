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


D = ((-1, 0), (1, 0), (0, -1), (0, 1))

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    R, C = map(int, input().split())
    M = [list(input().strip()) for _ in range(R)]
    vis = [[False for _ in range(C)] for _ in range(R)]

    ji, jj = -1, -1
    F = []

    for i in range(R):
        for j in range(C):
            if M[i][j] == 'J':
                M[i][j] = 0
                ji = i
                jj = j

            if M[i][j] == 'F':
                M[i][j] = 0
                F.append((i, j))


    if F:
        dq = deque(F)
        while dq:
            x, y = dq.popleft()

            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    if M[nx][ny] == '.':
                        M[nx][ny] = M[x][y] + 1
                        dq.append((nx, ny))

    dq = deque([(ji, jj, 0)])
    vis[ji][jj] = True
    minTime = 10 ** 9

    while dq:
        x, y, time = dq.popleft()

        for dx, dy in D:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                minTime = min(minTime, time + 1)
                break
            else:
                m = M[nx][ny]
                if m != '#':
                    if m == '.' or time+1 < m:
                        if vis[nx][ny] == False:
                            vis[nx][ny] = True
                            dq.append((nx, ny, time+1))

    if minTime != 10 ** 9:
        print(minTime)
    else:
        print("IMPOSSIBLE")


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