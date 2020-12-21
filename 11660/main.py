import os
import sys
import itertools
import collections

DEBUG = False
if len(sys.argv) == 1:
    if os.path.exists("i"):
        DEBUG = True
        sys.stdin = open("i")
    
    if os.path.exists("in"):
        DEBUG = True
        sys.stdin = open("in/i")

    if os.path.exists("a"):
        sys.stdout = open("o", "w")

elif len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
else:
    assert False, "too many arguments"
input=sys.stdin.readline


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def ints(): return map(int, sys.stdin.readline().strip().split())


def createCumMat(mat):
    H = len(mat)
    W = len(mat[0])
    cumMat = [[0 for _ in range(W)] for _ in range(H)]
    cumMat[0][0] = mat[0][0]
    for i in range(1, H):
        for j in range(1, W):
            cumMat[i][j] = mat[i][j] +\
            cumMat[i-1][j] +\
            cumMat[i][j-1] -\
            cumMat[i-1][j-1]
    return cumMat

## ij    iy
## 
## 
## xj    xy
## 
## then, must be + (i-1, j-1)
## - i-1, y)
## - (x, j-1)
## + (x, y)

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
    global input
    if f is not None:
        sys.stdin = open(f)
        input=sys.stdin.readline
        dprint(f, "opened!")

    #mat = getMat()
    N, M = (int(i) for i in input().split())
    mat = [[0 for _ in range(N+1)]]\
        + [[int(j) for j in ("0 " + input()).split()] for _ in range(N)]
    
    
    cumMat = createCumMat(mat)
    for _ in range(M):
        args = list(map(int, input().split()))

        ret = solve(mat, cumMat, *args)
        print(ret)


def answer(mat, i, j, x, y):
    sum_ = 0
    for a in range(i, x+1):
        for b in range(j, y+1):
            sum_ += mat[a][b]
    return sum_


if __name__ == "__main__":
    main()