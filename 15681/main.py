# CP template Version 1.005
import os
import sys
sys.setrecursionlimit(10**9)
DEBUG = False

input = sys.stdin.readline

N, R, Q = map(int, input().split())
R -= 1
g = [[] for _ in range(N)]

for _ in range(N-1):
    #U, V = map(lambda x: int(x)-1, input().split())
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    g[U].append(V)
    g[V].append(U)

size = [None] * N

def sizeOf(node):
    size[node] = 1
    for nbr in g[node]:
        if not size[nbr]:
            sizeOf(nbr)
            size[node] += size[nbr]

sizeOf(R)

for _ in range(Q):
    q = int(input())-1
    print(size[q])