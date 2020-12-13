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
    N, M = (int(i) for i in input().split())
    mat = [list(input().strip()) for _ in range(N)]

    trans = [[None for _ in range(N)] for _ in range(M)]

    froms = '-|/\\^<v>'
    tos =   '|-\\/<v>^'
    chg = {i:j for i, j in zip(froms, tos)}

    for i in range(N):
        for j in range(M):
            c = mat[i][j]
            if c in chg:
                mat[i][j] = chg[c]

    for i in range(N):
        for j in range(M):
            trans[j][i] = mat[i][j]
    
    trans.reverse()

    for i in trans:
        print(''.join(i))





if __name__ == "__main__":
    main()