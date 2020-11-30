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


import copy
def createCumMat(mat):
    cumMat = copy.deepcopy(mat)
    H = len(mat)
    W = len(mat[0])
    for i in range(1, H):
        for j in range(1, W):
            cumMat[i][j] = mat[i][j] +\
            cumMat[i-1][j] +\
            cumMat[i][j-1] -\
            cumMat[i-1][j-1]
    return cumMat

def solve(mat, cumMat, i, j, x, y):
    return cumMat[x][y]\
    + cumMat[i-1][j-1]\
    - cumMat[x][j-1]\
    - cumMat[i-1][y]

def getMat():
    N, M = (int(i) for i in input().split())
    mat = [[0 for _ in range(M+1)]]\
        + [[i for i in (int(j) for j in ("0 " + input()).split())] for _ in range(N)]
    return mat


def main(f = None):
    init(f)

    mat = getMat()
    cumMat = createCumMat(mat)
    for _ in range(int(input())):
        args = list(map(int, input().split()))

        ret = solve(mat, cumMat, *args)
        ans = answer(mat, *args)
        assert ret == ans, "something wrong with %d %d" % (ret, ans)
        print(ret)


def answer(mat, i, j, x, y):
    sum_ = 0
    for a in range(i, x+1):
        for b in range(j, y+1):
            sum_ += mat[a][b]
    return sum_


if __name__ == "__main__":
    main()