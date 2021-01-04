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
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    queries = [list(map(int, i.split())) for i in sys.stdin.readlines()]

    st = SegTree(arr)

    for q in queries:
        pass

class SegTree:
    def __init__(s, arr):
        s.arr = arr

        n = len(arr)
        s.n = n

        tree = [0] * len(arr) * 2
        tree[n:] = arr[:]
        s.tree = tree

        for i in range(n-1, 0, -1):
            tree[i] = min(tree[i*2], tree[i*2+1])

    def query(l, r):
        min_ = 2 << 30 - 1
        if (l & 1):
              l -= 1






if __name__ == "__main__":
    main()