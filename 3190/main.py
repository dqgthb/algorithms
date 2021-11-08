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

    N = int(input())
    mat = Mat(N, N, 0)
    K = int(input())
    for _ in range(K):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        mat[x][y] = 1

    L = int(input())
    turns = []
    for _ in range(L):
        sec, turn = input().split()
        sec = int(sec)
        if turn == 'L': turn = -1
        else: turn = 1
        turns.append((sec, turn))
    turns.reverse()

    x, y = 0, 0
    mat[x][y] = 2
    snake = deque()
    snake.append((x, y))

    d = ((-1, 0), (0, 1), (1, 0), (0, -1))
    direction = 1
    time = 0

    while True:
        parr(mat)
        print()

        time += 1
        dx, dy = d[direction]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            print(time)
            return

        if mat[nx][ny] == 2:
            print(time)
            return


        if mat[nx][ny] == 1:
            mat[nx][ny] = 2
            x, y = nx, ny
            snake.append((x, y))
        else:
            mat[nx][ny] = 2
            x, y = nx, ny
            snake.append((x, y))
            tx, ty = snake.popleft()
            mat[tx][ty] = 0


        if turns:
            sec, turn = turns[-1]
            if sec == time:
                direction = (direction + turn) % 4
                turns.pop()



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