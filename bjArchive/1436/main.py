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
    N = int(input().strip())
    i = 1
    num = 666
    while True:
        if "666" in str(num):
            if i == N:
                break
            else:
                i += 1
        num+=1
    print(num)

if __name__ == "__main__":
    main()