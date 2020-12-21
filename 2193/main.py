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

def numOfPinaryNum(n):
    if n == 1: return 1
    if n == 2: return 1
    return 1 + numOfPinaryNum(n-2)

def main(f = None):
    init(f)
    N = int(input().strip())
    global dp
    dp = [None for _ in range(91)]
    dp[1] = 1
    dp[2] = 1
    ans = numOfPinaryNum(N)
    print(ans)


if __name__ == "__main__":
    main()