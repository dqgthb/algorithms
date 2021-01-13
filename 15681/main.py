# CP template Version 1.005
import sys
sys.setrecursionlimit(10**9)
DEBUG = False

def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def dprint(*args):
    if DEBUG: print(*args)

def pfast(*args, end = "\n", sep=' '): sys.stdout.write(sep.join(map(str, args)) + end)

def parr(arr):
    for i in arr:
        print(i)

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