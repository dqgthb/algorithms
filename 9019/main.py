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

    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        print(solve(a, b))

    # ######## INPUT AREA END ############


def solve(a, b):
    count = [None] * 10000

    dq = deque()
    dq.append(a)
    count[a] = ''

    def addWithLetter(num, prev, l):
        if count[num] == None:
            count[num] = count[prev] + l
            dq.append(num)


    while dq:
        c = dq.popleft()
        if c == b:
            return count[c]

        d = c * 2 % 10000
        addWithLetter(d, c, 'D')

        s = (c - 1) % 10000
        addWithLetter(s, c, 'S')

        sc = str(c)
        tmp = '0' * (4 - len(sc)) + sc
        l = tmp[1:] + tmp[0]
        l = int(l)
        r = tmp[3] + tmp[:3]
        r = int(r)
        addWithLetter(l, c, 'L')
        addWithLetter(r, c, 'R')






# #######


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