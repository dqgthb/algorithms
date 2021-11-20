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

    global N, A, min_, papers
    N = 10
    A = [list(map(int, input().split())) for _ in range(N)]
    papers = [5, 5, 5, 5, 5]

    # ######## INPUT AREA END ############

    min_ = 10**9
    solve(0, 0, 0)

    print(min_)



def canPaste(i, j, k):
    if i + k > N or j + k > N:
        return False

    for i in range(i, i+k):
        for j in range(j, j+k):
            if A[i][j] == 0:
                return False
    return True


def update(i, j, k, v):
    for i in range(i, i + k):
        for j in range(j, j + k):
            A[i][j] = v


def solve(i, j, cnt) -> None:
    print("solve", i, j)
    global min_

    allZero = True
    while True:
        print(i, j)
        if A[i][j] == 1:
            print("A",i, j, "isone")
            allZero = False
            break
        j += 1
        if j == N:
            j = 0
            i += 1
            if i == N:
                break

    if allZero:
        print("cnt is", cnt)
        min_ = min(min_, cnt)
    else:
        for k in range(5, 0, -1):
            if papers[k-1] > 0:
                if canPaste(i, j, k):
                    papers[k-1] -= 1
                    update(i, j, k, 0)
                    print(cnt, "paste", i, j, k)
                    solve(i, j, cnt+1)
                    update(i, j, k, 1)
                    papers[k-1] += 1





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