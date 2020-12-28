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

def main(f = None):
    init(f)
    T = int(input())

    for _ in range(T):
        N = int(input())
        G = [[] for _ in range(N)]
        parents = [None for _ in range(N)]
        for _ in range(N-1):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            G[a].append(b)
            parents[b] = a
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        g = Graph(G, parents)
        ans = g.solve(A, B)
        print(ans+1)

class Graph():
    def __init__(s, graph, parents):
        s.g = graph
        s.n = len(graph)
        s.parents = parents
        s.updateRoot()
        s.updateDepth()
    
    def updateRoot(s):
        curr = 0
        while s.parents[curr] is not None:
            curr = s.parents[curr]
        s.root = curr

    def updateDepth(s):
        depthArr = [0 for _ in range(s.n)]
        vis = [False for _ in range(s.n)]
        s._bfs(depthArr, vis, s.root, 0)
        s.depth = depthArr

    def _bfs(s, depthArr, vis, node, d = 0):
        q = collections.deque()
        q.append((node, d))
        added = [False for _ in range(s.n)]
        
        while q:
            node, d = q.popleft()
            # if vis[node]: return
            vis[node] = True
            depthArr[node] = d
            for i in s.g[node]:
                if not vis[i] and not added[i]:
                    q.append((i, d+1))
                    added[i] = True

    def solve(s, a, b):
        da = s.depth[a]
        db = s.depth[b]
        if db > da:
            a, b = b, a
            db, da = da, db
        
        while a is not None and s.depth[a] > db:
            a = s.parents[a]
        
        while a != b:
            a = s.parents[a]
            b = s.parents[b]
        
        return a


if __name__ == "__main__":
    main()