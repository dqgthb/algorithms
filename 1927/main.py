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
    t = int(input().strip())
    import heapq
    h = []
    for _ in range(t):
        i = int(input().strip())
        if i == 0:
            if len(h):
                print(heapq.heappop(h))
            else:
                print(0)
        else:
            heapq.heappush(h, i)





if __name__ == "__main__":
    main()