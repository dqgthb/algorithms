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

def buildGraph(n):
    G = [[] for i in range(n)]
    for _ in range(n-1):
        i, j = (int(i) for i in input().split())
        i -= 1
        j -= 1
        G[i].append(j)
        G[j].append(i)
    return G

def dfs(nodeNum:int):
    global G, visited, paren
    neighbors = G[nodeNum]
    for node_ in neighbors:
        if not visited[node_]:
            paren[node_] = nodeNum
            dfs(nodeNum)

def main(f = None):
    init(f)

    n = int(input().strip())
    global G, visited, paren
    G = buildGraph(n)
    for i in G:
        print(i)
    
    visited = [False for _ in range(n)]
    paren = [None for _ in range(n)]

    visited[0] = True
    dfs(0)

    for i in paren[1:]:
        print(i+1)


if __name__ == "__main__":
    main()