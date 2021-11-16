# CP template Version 1.006
#import os
#from sys import stdin
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque, Counter, defaultdict as dd
from collections import deque
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br

def main(f=None):
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global tMat
    tMat = [[None] * 3 for _ in range(3)]
    mat = [list(int(i) for i in input().split()) for _ in range(3)]
    desE = 123456780


    # ######## INPUT AREA END ############

    dq = deque()
    vis = set()
    matE = encode(mat)
    if matE == desE:
        print(0)
        return

    for i in range(3):
        for j in range(3):
            if mat[i][j] == 0:
                dq.append((matE, i*3 + j, 0))

    while dq:
        m, zeroPos, cnt = dq.popleft()

        base = 10 ** 8
        for i in range(3):
            for j in range(3):
                q, m = divmod(m, base)
                base //= 10
                tMat[i][j] = q


        i, j = divmod(zeroPos, 3)

        for n in range(4):
            di, dj = dir[n]
            ni, nj = i + di, j + dj

            if 0 <= ni < 3 and 0 <= nj < 3:
                tMat[i][j] = tMat[ni][nj]
                tMat[ni][nj] = 0

                val = 0
                base = 10 ** 8
                for a in range(3):
                    for b in range(3):
                        val += base * tMat[a][b]
                        base //= 10
                nmE = val

                nzero = 3 * ni + nj

                if nmE == desE:
                    print(cnt+1)
                    return
                if not nmE in vis:
                    vis.add(nmE)
                    dq.append((nmE, nzero, cnt+1))

                tMat[ni][nj] = tMat[i][j]
                tMat[i][j] = 0

    print(-1)


def encode(mat):
    val = 0
    base = 10 ** 8
    for i in range(3):
        for j in range(3):
            val += base * mat[i][j]
            base //= 10
    return val

dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

# TEMPLATE ###############################


if __name__ == "__main__":
    main()
