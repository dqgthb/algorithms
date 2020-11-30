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
    N = int(input().strip())
    arr = [[int(i) for i in input().split()] for _ in range(N)]
    arr.sort(key = lambda x:x[0])
    arr.sort(key = lambda x:x[1])

    count = 0
    end = 0
    for s,e in arr:
        if end <= s:
            count += 1
            end = e
    print(count)





if __name__ == "__main__":
    main()