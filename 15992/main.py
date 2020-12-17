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

MOD = 1000000009

def solve(n, m):
    if m == 0:
        return 0
    
    if n <= 0:
        return 0

    global dp
    if dp[n][m] is not None:
        return dp[n][m]

    sum_ = 0 
    for i in range(1, 4):
        sum_ += solve(n-i, m-1)
        sum_ %= MOD
    dp[n][m] = sum_
    return sum_


def main(f = None):
    global dp
    init(f)
    T = int(input().strip())
    dp = [[None for _ in range(1001)] for _ in range(1001)]
    dp[1][1] = 1
    dp[2][1] = 1
    dp[3][1] = 1

    for l in map(lambda x: x.strip(), sys.stdin):
        n, m = (int(i) for i in l.split())
        ans = solve(n, m)
        print(ans)

if __name__ == "__main__":
    main()