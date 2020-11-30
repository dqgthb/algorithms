import os
import sys
import itertools
import collections
TEST = ''
DEBUG = False
if os.path.exists("i" + TEST):
    DEBUG = True
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)
input=sys.stdin.readline


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def ints(): return map(int, sys.stdin.readline().strip().split())


def main():
    mat = [[i for i in input().strip()] for _ in range(5)]
    print(mat)

    origin = [['' for _ in range(15)] for _ in range(5)]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            origin[i][j] = mat[i][j]

    print(origin)

    trans = [['' for _ in range(5)] for _ in range(15)]

    for i in range(15):
        for j in range(5):
            trans[i][j] = origin[j][i]

    arr = ''.join(''.join(trans[i]) for i in range(15))
    print(arr)


if __name__ == "__main__":
    main()