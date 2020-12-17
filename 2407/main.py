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

def co(n, r):
    global dp
    if dp[n][r] is not None: return dp[n][r]
    if r == n: return 1
    if r == 0: return 1

    dp[n][r] = co(n-1, r-1) + co(n-1, r)
    return dp[n][r]

def main(f = None):
    init(f)
    global dp
    dp = [[None for _ in range(101)] for _ in range(101)]
    n, m = (int(i) for i in input().split())
    print(co(n, m))


if __name__ == "__main__":
    main()