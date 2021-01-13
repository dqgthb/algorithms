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

def compare(x, y):
    weight = 0
    height = 1

    if (x[weight] > y[weight]
            and x[height] > y[height]):
        return 1
    elif (
            y[weight] > x[weight]
            and y[height] > x[height]):
        return -1
    else:
        return 0

def main():
    N = int(input().strip())
    arr = [list(int(i) for i in input().split()) for _ in range(N)]

    for i in arr:
        i.append(1)

    rank = len(arr[0]) - 1
    for i, j in itertools.combinations(arr, 2):
        c = compare(i,j)
        if c == 1:
            j[rank] += 1
        elif c == -1:
            i[rank] += 1
    
    for i in arr:
        print(i[rank])

if __name__ == "__main__":
    main()
