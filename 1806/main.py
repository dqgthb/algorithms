import os
import sys
import itertools
import collections

DEBUG = False

def setStdin(f):
    global DEBUG
    global input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
    if os.path.exists("o"):
        sys.stdout = open("o", "w")

    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:

            if os.path.isfile("in/i"):
                setStdin("in/i")

            elif os.path.isfile("i"):
                setStdin("i")

        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])

        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)

def dprint(*args):
    if DEBUG:
        print(*args)

def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)

def ints(): return map(int, sys.stdin.readline().rstrip().split())

def main(f = None):
    init(f)
    N, S = (int(i) for i in input().split())
    arr = [int(i) for i in input().split()]

    min_ = 100001

    l, h = 0, 0
    sum_ = 0
    while h < N:
        if sum_ < S:
            sum_ += arr[h]
            h += 1
        else:
            min_ = min(min_, h - l + 1)
            sum_ -= arr[l]
            l += 1
            if l >= h:
                h += 1
    print(min_)




if __name__ == "__main__":
    main()