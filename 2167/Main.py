import os
import sys
import itertools
import collections

DEBUG = False
if len(sys.argv) == 1:
    if os.path.exists("i"):
        DEBUG = True
        sys.stdin = open("i")
    elif os.path.isdir("in"):
        DEBUG = True

    if os.path.exists("a"):
        sys.stdout = open("o", "w")

elif len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
    DEBUG = True
else:
    assert False, "too many arguments"
input=sys.stdin.readline

DEBUG=False


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def solve(mat):
    pass


def main(f = None):
    global input
    if f is not None:
        sys.stdin = open(f)
        input=sys.stdin.readline
        dprint(f, "opened!")

    N, M = (int(i) for i in input().split())

    mat = [[i for i in (int(i) for i in input().split())] for _ in range(N)]

    import copy
    cumMat = copy.deepcopy(mat)
    for i in range(1, N):
        cumMat[i][0] = cumMat[i-1][0] + mat[i][0]
    for j in range(1, M):
        cumMat[0][j] = cumMat[0][j-1] + mat[0][j]
    for i in range(1, N):
        for j in range(1, M):
            cumMat[i][j] = cumMat[i][j-1] + cumMat[i-1][j] - cumMat[i-1][j-1] + mat[i][j]

    K = int(input().strip())
    dprint("K is", K)

    for _ in range(K):
        i, j, x, y = (int(i)-1 for i in input().split())
        ans = 0
        if i == 0 and j == 0:
            ans = cumMat[x][y]
        elif i == 0:
            ans = cumMat[x][y] - cumMat[x][j-1]
        elif j == 0:
            ans = cumMat[x][y] - cumMat[i-1][y]
        else:
            ans = cumMat[x][y] - cumMat[x][j-1] - cumMat[i-1][y] + cumMat[i-1][j-1]
        sumMat_ = sumMat(mat, i, j, x, y)
        dprint(ans, "must be the same as", sumMat_)
        assert ans == sumMat_, "{} not equal {}".format(ans, sumMat_)
        print(ans)


def sumMat(mat, i, j, x, y):
    sum_ = 0

    for r in range(i, x+1):
        for c in range(j, y+1):
            sum_ += mat[r][c]
    
    return sum_


if __name__ == "__main__":
    main()
