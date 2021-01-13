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


class Point:
    def __init__(self, i, v):
        self.i = i
        self.v = v
        self.c = 0
    
    def __str__(self):
        return 'Point<'+' '.join(map(str, (self.i, self.v, self.c)))+'>'
    def __repr__(self):
        return self.__str__()

def main():
    N = int(input().strip())
    arr = [Point(i, int(e)) for i, e in enumerate(input().split())]
    arr.sort(key = lambda x : x.v)
    
    seq = arr[0].c = 0
    for i in range(1, len(arr)):
        curr = arr[i]
        prev = arr[i-1]

        assert curr.v >= prev.v, "not sorted"

        if curr.v > prev.v:
            seq += 1
        arr[i].c = seq

    arr.sort(key = lambda x : x.i)
    str_ = ' '.join(str(i.c) for i in arr)
    print(str_)


if __name__ == "__main__":
    main()
