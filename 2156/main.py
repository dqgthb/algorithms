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


def solve(arr, lastIndex):
    x = lastIndex

class DP:
    def __init__(s, arr):
        s.arr =arr
        s.n = len(arr)
        s.dp = [None] * s.n
    
    def solve(s, lastIndex):
        x = lastIndex
        dp = s.dp
        a = s.arr
        val = dp[x]
        if val is not None:
            return val
        
        if x < 2:
            return a[:x]
        
        c1 = solve(s, lastIndex - 2) + a[x]
        c2 = solve(s, lastIndex - 1)
        c3 = solve(s, lastIndex - 3)

def main(f = None):
    init(f)
    n = int(input())
    arr = [int(input()) for _ in range(n)]


if __name__ == "__main__":
    main()