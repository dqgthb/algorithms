# CP template Version 1.006
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
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    # ###nennno##### INPUT AREA BEGIN ##########

    global N, M, G, V, A, B
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(N):
        a, *arr = map(int, input().split())
        for b in arr:
            G[i].append(b-1)

    cnt = 0
    A = [None] * N
    B = [None] * M
    V = [False] * N

    for i in range(N):
        for b in G[i]:
            if B[b] is None:
                B[b] = i
                A[i] = b
                cnt += 1
                break


    for i in range(N):
        if A[i] is not None:
            continue
        for j in range(N):
            V[j] = False
        if dfs(i):
            cnt += 1

    print(cnt)


def dfs(a):
    V[a] = True

    for b in G[a]:
        if B[b] is None or not V[B[b]] and dfs(B[b]):
            A[a] = b
            B[b] = a
            return True
    return False

    # ######## INPUT AREA END ############


# TEMPLATE ###############################




if __name__ == "__main__":
    main()