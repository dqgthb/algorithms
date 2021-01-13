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

N = int(input().strip())

mat = [list(input().strip()) for _ in range(N)]

def main():
    n = N
    mat.append(list('X' * (n+1)))
    for i in range(n):
        mat[i].append('X')
    
    r = 0
    c = 0
    for i in range(n):
        for j in range(n-1):
            if (mat[i][j] == '.'
            and mat[i][j+1] == '.'
            and mat[i][j+2] == 'X'):
                r += 1

            if (mat[j][i] == '.'
            and mat[j+1][i] == '.'
            and mat[j+2][i] == 'X'):
                c += 1
    print(r, c)


if __name__ == "__main__":
    main()
