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
    n = int(input().strip())
    b = [int(input()) for _ in range(n)]
    h = [None for _ in range(n)]
    dp = [0 for _ in range(n)]

    for i in range(len(b)-2, -1, -1):
        e = b[i]
        prevIdx = i+1
        prevVal = b[prevIdx]
        if e <= prevVal:
            dp[i] = 0
            h[i] = i+1 # higher is i+1
        else:
            while prevIdx < len(b):
                higherThanPrevIdx = h[prevIdx]
                if higherThanPrevIdx is None:
                    dp[i] = len(b) - i - 1
                    h[i] = None
                    break
                if b[higherThanPrevIdx] >= e:
                    dp[i] = higherThanPrevIdx - i - 1
                    h[i] = higherThanPrevIdx
                    break
                else:
                    prevIdx = higherThanPrevIdx
    print(sum(dp))




if __name__ == "__main__":
    main()