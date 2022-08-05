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

def solve(mat):
    h, w = len(mat), len(mat[0])

    acc = 1
    for i in range(w):
        for j in range(h-1, -1, -1):
            if mat[j][i] == 1:
                mat[j][i] = acc
                acc += 1
        acc = 1
    
    #cols = [0 for _ in range(w)]
    for i in range(h):
        for j in range(w):
            mat[i][j]

    for l in mat:
        print(l)

    return None

def main(f = None):
    init(f)
    t = int(input().strip())
    for _ in range(t):
        h, w = (int(i) for i in input().split())
        mat = [[int(i) for i in input().split()] for _ in range(h)]
        ans = solve(mat)
        print(ans)

if __name__ == "__main__":
    main()