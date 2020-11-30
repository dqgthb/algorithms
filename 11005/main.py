import os
import sys
import itertools
import collections
DEBUG = False

if os.path.exists("i"):
    DEBUG = True
    sys.stdin = open("i")
if os.path.exists("a"):
    sys.stdout = open("o", "w")
input=sys.stdin.readline

if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
    input=sys.stdin.readline


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def ints(): return map(int, sys.stdin.readline().strip().split())


import string
lookup = string.digits + string.ascii_uppercase

def solve(N, B):
    arr = []

    while N != 0:
        q, r = divmod(N, B)
        arr.append(r)
        N = q

    res = ''.join(lookup[i] for i in reversed(arr))
    print(res)

def main():

    if len(sys.argv) == 2:
        sys.stdin = open(sys.argv[1])
    input=sys.stdin.readline
    N, B = (int(i) for i in input().split())
    solve(N, B)
    '''

    for i in range(1, 10):
        for j in range(2, 10):
            solve(i, j)
    '''



if __name__ == "__main__":
    main()