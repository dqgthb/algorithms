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
    N = int(input().strip())

    sum_ = 0
    for i in range(1, N):
        sum_ += i*N + i
    
    print(sum_)



if __name__ == "__main__":
    main()