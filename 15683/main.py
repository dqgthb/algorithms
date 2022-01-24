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


d = ((-1, 0), (0, 1), (1, 0), (0, -1)) # NESW
def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global N, M, m, camLoc, minDeadSight
    N, M = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]

    camLoc = []
    for i in range(N):
        for j in range(M):
            if 0 < m[i][j] < 6:
                camLoc.append((i, j, m[i][j]))

    c = [i[:] for i in m]
    minDeadSight = 10 ** 9
    draw(0, c)
    print(minDeadSight)


def countDeadSight(map_):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if map_[i][j] == 0:
                cnt += 1
    return cnt


def draw(n, mapState):
    global minDeadSight
    if n == len(camLoc):
        deadSight = countDeadSight(mapState)
        if minDeadSight > deadSight:
            minDeadSight = deadSight
        return

    i, j, type_ = camLoc[n]
    if type_ == 5:
        newMapState = drawCameraVision(mapState, i, j, type_, 0)
        draw(n+1, newMapState)
    elif type_ == 2:
        for direction in range(2):
            newMapState = drawCameraVision(mapState, i, j, type_, direction)
            draw(n+1, newMapState)
    else: # for 1, 3, 4
        for direction in range(4):
            newMapState = drawCameraVision(mapState, i, j, type_, direction)
            draw(n+1, newMapState)

    # ######## INPUT AREA END ############


def drawCameraVision(map_, i, j, type_, direction):
    map_ = [i[:] for i in map_]
    if type_ == 1:
        map_ = drawLineVision(map_, i, j, direction)

    elif type_ == 2:
        map_ = drawLineVision(map_, i, j, direction)
        map_ = drawLineVision(map_, i, j, (direction+2) % 4)

    elif type_ == 3:
        map_ = drawLineVision(map_, i, j, direction)
        map_ = drawLineVision(map_, i, j, (direction+1) % 4)

    elif type_ == 4:
        skip = direction
        for direction in range(4):
            if direction != skip:
                map_ = drawLineVision(map_, i, j, direction)

    elif type_ == 5:
        assert direction == 0
        for direction in range(4):
            map_ = drawLineVision(map_, i, j , direction)

    return map_


def drawLineVision(map_, i, j, direction):
    di, dj = d [direction]
    while True:
        i, j = i + di, j + dj
        if not (0 <= i < N and 0 <= j < M):
            break
        if map_[i][j] == 6:
            break
        if map_[i][j] == 0:
            map_[i][j] = 7
    return map_


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