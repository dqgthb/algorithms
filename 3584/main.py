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
        G = [[False for _ in range(N)] for _ in range(N)]
        parents = [None for _ in range(N)]
        for _ in range(N-1):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            G[a][b] = True
            parents[b] = a
        A, B = map(int, input().split())
        g = Graph(G, parents)
        ans = g.solve(A, B)
        print(ans)

class Graph():
    def __init__(s, graph, parents):
        s.g = graph
        s.n = len(graph)
        s.parents = parents
    
    def getRoot(s):
        curr = 0

    
    def depth(s):
        s.d = [None for _ in range(s.n)]
    
    def _bfs(s):

    
    def solve(s, A, B):
        return 0

if __name__ == "__main__":
    main()