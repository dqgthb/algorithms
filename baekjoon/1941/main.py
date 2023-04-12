# Python Competitive Programming Template (updated 2022-08-05)
# Created by dqgthb

#from collections import deque
#from heapq import heappush, heappop

from itertools import combinations

#from functools import cmp_to_key, reduce, partial
#from collections import Counter, defaultdict as dd
#from math import log, log2, ceil, floor, gcd, sqrt
#from bisect import bisect_left as bl, bisect_right as br


D = ((-1, 0), (1, 0), (0, -1), (0, 1))


def connected(c):
    P = [i for i in range(25)]
    cij = [(i//5, i % 5) for i in c]
    for i in range(7):
        for j in range(i+1, 7):
            x, y = cij[i]
            xx, yy = cij[j]

            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if (xx, yy) == (nx, ny):
                    union(P, c[i], c[j])

    p0 = find(P, c[0])
    for i in range(1, 7):
        if find(P, c[i]) != p0:
            return False
    return True


def find(P, x):
    if P[x] == x:
        return x
    else:
        P[x] = find(P, P[x])
        return P[x]


def union(P, x, y):
    fx = find(P, x)
    fy = find(P, y)
    if fx < fy:
        P[fy] = fx
    else:
        P[fx] = fy


def main():
    init()
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global D

    M = [[i for i in input().strip()] for _ in range(5)]

    cnt = 0
    for c in combinations(range(25), r=7):
        print(c)
        P = [(i // 5, i % 5) for i in c]
        cntS = sum(1 if M[i][j] == 'S' else 0 for i, j in P)
        if cntS >= 4:
            if connected(c):
                # print(P)
                cnt += 1
    # print(ans)
    print(cnt)


# TEMPLATE ###############################


def parr(arr):
    print('\n'.join(str(i) for i in arr))


def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]


def init():
    global input
    from sys import stdin, argv
    input = stdin.readline  # by default

    if len(argv) == 1:
        from os import path
        if path.isfile("i"):
            stdin = open("i")
            input = stdin.readline

    elif len(argv) == 2:
        stdin = open(argv[1])
        input = stdin.readline


if __name__ == "__main__":
    main()
