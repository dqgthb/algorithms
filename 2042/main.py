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

class SegTree:
    def __init__(s, arr):
        s.arr = arr
        s.tree = [None]
    
    def update(s, idx, val):


def main(f = None):
    init(f)
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    print(arr)
    tree = [None for _ in range(4 * len(arr))]

    s = SegTree(arr)
    for i in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            s.update(b, c)
        else:
            ans = s.rangeSum(b, c)
            print(ans)




if __name__ == "__main__":
    main()