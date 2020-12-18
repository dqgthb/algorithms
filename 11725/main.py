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

    N = int(input().strip())
    mat = [[False for _ in range(N)] for _ in range(N)]
    global visited
    visited = [False for _ in range(N)]

    for _ in range(N-1):
        i, j = (int(i) for i in input().split())
        i -= 1
        j -= 1
        mat[i][j] = True
        mat[j][i] = True

    paren = [None for _ in range(N)]
    root = 0
    visited[root] = True
    dfs(mat, paren, root)

    for i in paren[1:]:
        print(i+1)

def dfsGeneral(mat, visited, node, action):
    if visited[node]:
        return
    visited[node] = True
    action()

    nodes = mat[node]
    for i, isNeighbor in enumerate(nodes):
        if isNeighbor and not visited[i]:



def dfs(mat, paren, start):
    global visited
    neighbors = mat[start]
    for i, isNeighbor in enumerate(neighbors):
        if isNeighbor and not visited[i]:
            visited[i] = True
            paren[i] = start
            dfs(mat, paren, i)


if __name__ == "__main__":
    main()