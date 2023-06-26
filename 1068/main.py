# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from sys import stdin, argv
from os import path

# from collections import deque
# from heapq import heappush, heappop
# from math import log, log2, ceil, floor, gcd, sqrt
# from bisect import bisect_left as bl, bisect_right as br


def main() -> None:
    # sys.setrecursionlimit(10**9)

    global N, arr, G, M, cnt
    N = int(input())
    arr = list(map(int, input().split()))

    G = [[] for _ in range(N)]

    root = 0
    for i in range(N):
        parent = arr[i]

        if parent == -1:
            root = i
        else:
            G[parent].append(i)
    M = int(input())

    G[M] = []

    cnt = 0

    if root != M:
        dfs(root)

    print(cnt)


def dfs(node):
    global cnt

    if not G[node]:
        cnt += 1
        return

    if len(G[node]) == 1 and G[node][0] == M:
        cnt += 1
        return

    for n in G[node]:
        if n != M:
            dfs(n)


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
