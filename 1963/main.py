# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
import itertools
#from itertools import product
#import collections
#from collections import deque, Counter, defaultdict as dd
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

    global T, sieve, primes, G, convert, N
    T = int(input())
    sieve = [True] * 10000
    sieve[0] = False
    sieve[1] = False
    for i in range(2, 10000):
        factor = 2
        while True:
            v = i * factor
            if v >= 10000:
                break
            sieve[v] = False
            factor += 1

    primes = []
    for i in range(1000, 10000):
        if sieve[i]:
            primes.append(i)
    N = len(primes)
    convert = {primes[i]:i for i in range(N)}
    G = [[] for _ in range(N)]
    preprocess()

    for _ in range(T):
        a, b = map(int, input().split())
        solve(a, b)

    # ######## INPUT AREA END ############

def preprocess():
    for i in range(N):
        prime = primes[i]
        lst = [0, 0, 0, 0]
        orig = [int(i) for i in str(prime)]

        for digit in range(4):
            lst[:] = orig
            for num in range(10):
                lst[digit] = num
                val = int(''.join(map(str, lst)))
                if val > 999 and sieve[val]:
                    G[i].append(convert[val])
    print(G)





def solve(a, b):
    pass


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