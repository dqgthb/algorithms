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
    N, K = (int(i) for i in input().split())
    dq = collections.deque(range(1, N+1))

    arr = []
    while len(dq) > 0:
        for _ in range(K-1):
            dq.append(dq.popleft())
        arr.append(dq.popleft())
    toStr = ', '.join(map(str, arr))
    print("<"+toStr+">")




if __name__ == "__main__":
    main()