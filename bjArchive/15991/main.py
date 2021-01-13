import os
import sys
import itertools
import collections

DEBUG = False
MOD = 1000000009

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

def solve(n):
    """number of cases"""
    if n < 0: return 0

    global dp
    if dp[n] is not None:
        return dp[n]

    assert n > 4

    sum_ = 0
    for i in range(1, 4):
        sum_ += solve(n-2*i) % MOD
    dp[n] = sum_ % MOD
    return sum_ % MOD

def main(f = None):
    init(f)
    pass

if __name__ == "__main__":
    main()


def main(f = None):
    global dp
    init(f)
    dp = [None for _ in range(100001)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 2
    dp[4] = 3
    for i in range(100001):
        solve(i)
    
    t = int(input().strip())
    for l in sys.stdin:
        l = int(l.strip())
        ans = solve(l)
        print(ans)

if __name__ == "__main__":
    main()