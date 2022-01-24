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

    global gears
    gears = [0] * 4
    for i in range(4):
        gears[i] = int(input(), 2)

    K = int(input())
    for _ in range(K):
        n, d = map(int, input().split())
        rotate(n-1, d < 0)

    # ######## INPUT AREA END ############


def cr(a):
    return (a >> 1) | ((a & 1) << 7)


def ccr(a):
    return (a << 1) & ~(1 << 8) | ((a & (1 << 7)) >> 7)


def rotate(gearNo, isCcr):
    global gears
    a, b, c, d = *gears
    x, y, z, w = 0, 0, 0, 0
    if gearNo == 0:
        x = ccr(a) if isCcr else cr(a)
        y = rotateByLeft(b, a, isCcr)



def rotateByLeft(currGear, leftGear, isLeftCcr):
    isCPoleSouth = currGear & (1 << 6) > 0
    isLPoleSouth = leftGear & (1 << 2) > 0

    # no rotation
    if isCPoleSouth == isLPoleSouth:
        return currGear

    if isLeftCcr:
        return cr(currGear)
    else:
        return ccr(currGear)


def rotateByRight(currGear, leftGear, isRightCcr):
    isCPoleSouth = currGear & (1 << 2) > 0
    isLPoleSouth = leftGear & (1 << 6) > 0

    # no rotation
    if isCPoleSouth == isLPoleSouth:
        return currGear

    if isRightCcr:
        return cr(currGear)
    return ccr(currGear)


# TEMPLATE ###############################


enu = enumerate


def For(*args):
    from itertools import product
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