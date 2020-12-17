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

dp = [None for _ in range(81)]
dp[0] = 1
dp[1] = 1
def fib(dp, n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    if dp[n] is not None:
        return dp[n]
    return fib(dp, n-1) + fib(dp, n-2)

def main(f = None):
    init(f)
    n = int(input().strip())
    ans = fib(dp, n + 1)
    print(ans * 2)

if __name__ == "__main__":
    main()