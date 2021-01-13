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
    _ = input()
    arr = [int(i) for i in input().split()]
    arr.sort()
    cumSum = list(arr)
    for i in range(1, len(cumSum)):
        cumSum[i] += cumSum[i-1]
    print(sum(cumSum))






if __name__ == "__main__":
    main()