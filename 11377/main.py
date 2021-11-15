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

    global N, M, K, G, NN, S, E, D, C, F
    N, M, K = map(int, input().split())

    G = [[] for _ in range(N + M + 3)]
    NN = N + M + 3

    S = N + M
    E = S + 1
    D = E + 1
    C = Mat(NN, NN, 0)
    F = Mat(NN, NN, 0)

    # connect S and D
    G[S].append(D)
    G[D].append(S)
    C[S][D] = K

    # connect S and N, D and N
    for i in range(N):
        G[S].append(i)
        G[i].append(S)
        C[S][i] = 1

        G[D].append(i)
        G[i].append(D)
        C[D][i] = 1

    # connect N and M
    for i in range(N):
        _, *arr = map(int, input().split())

        for j in arr:
            m = j + N - 1
            G[i].append(m)
            G[m].append(i)
            C[i][m] = 1

    for i in range(N, N + M):
        G[i].append(E)
        G[E].append(i)
        C[i][E] = 1


    totalFlow = 0
    while True:

        P = bfs()

        if P is not None:

            flow = 10 ** 9

            curr = E
            while curr != S:
                prev = P[curr]
                flow = min(flow, C[prev][curr] - F[prev][curr])
                curr = prev

            curr = E
            while curr != S:
                prev = P[curr]
                F[prev][curr] += 1
                F[curr][prev] -= 1
                curr = prev

            totalFlow += flow
        else:
            break
    print(totalFlow)


def bfs():
    P = [None] * NN
    P[S] = S
    dq = deque()

    dq.append(S)

    while dq:
        x = dq.popleft()

        for y in G[x]:
            if P[y] is None:
                if C[x][y] > F[x][y]:
                    P[y] = x
                    if y == E:
                        return P
                    dq.append(y)
    return None











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