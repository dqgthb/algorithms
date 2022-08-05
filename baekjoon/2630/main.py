import os
import sys
import itertools
import collections
TEST = ''
if os.path.exists("i" + TEST):
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)
input=sys.stdin.readline


def printe(*args,**kwargs):
    print(*args, **kwargs, file=sys.stderr)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


numB = 0
numW = 0
N = 0
mat = []

def checkColor(x, y, n):
    global numB, numW, N, mat
    if x >= N or y >= N:
        return
    first = mat[x][y]
    for i in range(x, n + x):
        for j in range(y, n + y):
            mv = mat[i][j]
            if mv != first:
                h = n // 2
                checkColor(x, y, h)
                checkColor(x + h, y, h)
                checkColor(x, y + h, h)
                checkColor(x + h , y + h, h)
                return
    if first:
        numB += 1
    else:
        numW += 1


def main():
    global N, mat
    N = int(input().strip())
    mat = [[bool(int(i)) for i in input().split()] for _ in range(N)]
    checkColor(0, 0, N)
    print(numW)
    print(numB)



if __name__ == "__main__":
    main()