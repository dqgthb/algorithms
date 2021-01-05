import os
import sys
import itertools
import collections

DEBUG = False

def setStdin(f):
    global DEBUG
    global input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
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

def dprint(*args):
    if DEBUG:
        print(*args)

def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)

def ints(): return map(int, sys.stdin.readline().rstrip().split())

class Graph:
    def __init__(s, g):
        s.g = g
        s.n = len(g)
        s.update()
    
    def update(s): # depth and parents info
        N = s.n
        depth = [None for _ in range(N)]
        added = [False for _ in range(N)]
        parents = [None for _ in range(N)]
        q = collections.deque()
        root = 0
        d = 0
        q.append((root, d, None))
        added[root] = True
        while q:
            node, d, parent = q.popleft()
            depth[node] = d
            parents[node] = parent
            for i in s.g[node]:
                if not added[i]:
                    q.append((i, d+1, node))
                    added[i] = True
        s.depth = depth
        s.parents = parents

    def lca(s, a, b):
        d = s.depth
        p = s.parents
        if d[a] < d[b]:
            a, b = b, a

        while d[a] > d[b]:
            a = p[a]

        while a != b:
            a = p[a]
            b = p[b]
        return a

def main(f = None):
    init(f)
    N = int(input())
    g = [[] for _ in range(N)]
    parents = [None for _ in range(N)]
    for _ in range(N-1):
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)
        g[b].append(a)
    
    graph = Graph(g)

    M = int(input())
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        ans = graph.lca(a, b)
        print(ans + 1)

if __name__ == "__main__":
    main()