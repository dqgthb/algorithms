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
    N = input().strip()
    Nlst = [int(i) for i in N]
    cntr = collections.Counter(Nlst)
    cntr[6] += cntr[9]
    cntr[9] = 0
    cntr[6] -= (cntr[6]//2)
    print(cntr.most_common(1)[0][1])



if __name__ == "__main__":
    main()