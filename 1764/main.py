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


def main():
    N, M = (int(i) for i in input().split())
    dud = set(input().strip() for _ in range(N))
    count = 0
    names = []
    for _ in range(M):
        ip = input().strip()
        if ip in dud:
            count += 1
            names.append(ip)
    print(count)
    names.sort()
    for i in names:
        print(i)



if __name__ == "__main__":
    main()