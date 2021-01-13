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


def F(n):
    return int(''.join(map(str, (9-int(a) for a in str(n)))))

def loveliness(n):
    return n * F(n)

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        l = len(str(n))
        up = 10 ** l
        half = up // 2
        if n > half:
            print(loveliness(half))
        else:
            print(loveliness(n))


if __name__ == "__main__":
    main()