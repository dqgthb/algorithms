# CP template Version .005
import os
import sys
sys.setrecursionlimit(987654321)
DEBUG = False

def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
    if os.path.exists("o"): sys.stdout = open("o", "w")
    if f is not None: setStdin(f)
    else:
        if len(sys.argv) == 1:
            assert False, "wrong!!"
            if os.path.isfile("in/i"): setStdin("in/i")
            elif os.path.isfile("i"): setStdin("i")
        elif len(sys.argv) == 2: setStdin(sys.argv[1])
        else: assert False, "Too many sys.argv: %d" % len(sys.argv)

def dprint(*args):
    if DEBUG: print(*args)

def pfast(*args, end = "\n", sep=' '): sys.stdout.write(sep.join(map(str, args)) + end)

init(None)

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