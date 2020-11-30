import os
import sys
import itertools
import collections

DEBUG = False
if len(sys.argv) == 1:
    if os.path.exists("i"):
        DEBUG = True
        sys.stdin = open("i")

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


def main():
    N, M = (int(i) for i in input().split())
    A = [list(int(i) for i in input().split()) for _ in range(N)]

    M2, K = (int(i) for i in input().split())
    assert M == M2, "wrong size"
    B = [list(int(i) for i in input().split()) for _ in range(M)]

    res = [[0 for _ in range(K)] for _ in range(N)]

    for i in range(N):
        for j in range(K):
            for k in range(M):
                res[i][j] += A[i][k] * B[k][j]

    for i in res:
        print(' '.join(map(str, i)))


if __name__ == "__main__":
    main()