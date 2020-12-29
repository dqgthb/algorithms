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
    
    n = int(input())
    edges = [[] for _ in range(n)]

    for _ in range(n-1):
        a, b, c = map(lambda x: int(x)-1, input().split())
        c += 1
        edges[a].append((b, c))
        edges[b].append((a, c))

    root = 0
    g = Graph(edges)
    x, d = g.getFarNode(0)
    y, d = g.getFarNode(x)
    print(d)

class Graph:
    def __init__(s, edges):
        s.e = edges
        s.n = len(edges)

    def getFarNode(s, from_):
        n = s.n
        vis = [False for _ in range(n)]
        distance = [None for _ in range(n)]
        #s.dfs(vis, distance, 0, from_)
        s.bfs(vis, distance, 0, from_)
        idx = distance.index(max(distance))
        return idx, distance[idx]

    def dfs(s, vis, distance, dist, from_):
        vis[from_] = True
        distance[from_] = dist
        for node, dis in s.e[from_]:
            if not vis[node]:
                s.dfs(vis, distance, dist + dis, node)
    
    def bfs(s, vis, distance, dist, from_):
        dq = collections.deque()
        vis[from_] = True
        dq.append((from_, dist))
        while dq:
            f, d = dq.popleft()
            distance[f] = d
            for node, dis in s.e[f]:
                if not vis[node]:
                    vis[node] = True
                    dq.append((node, dis + d))


if __name__ == "__main__":
    main()