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
    N = int(input().strip())
    A = (int(i) for i in input().split())
    last = [None for _ in range(N)]
    dp = [None for _ in range(N)]
    dp[0] = 1
    last[0] = A[0]

    for i in range(1, N):
        cand1 = 0
        if last[i-1] > A[i]:
            cand1 = dp[i-1] + 1
        cand2 = dp[i-1]
        if cand1 > cand2:
            dp[i] = cand1
            last[i] = A[i]


if __name__ == "__main__":
    main()