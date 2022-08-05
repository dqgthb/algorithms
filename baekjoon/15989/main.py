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

def endsWith(i, n):
    """ how many cases n ends with i """
    global dp
    assert i in (1, 2, 3)
    if n == 0:
        return 0

    dpVal = dp[n][i]
    if dpVal is not None:
        return dpVal

    if i == 1:
        dp[n][i] = endsWith(1, n-1)
    elif i == 2:
        dp[n][i] = endsWith(1, n-2) + endsWith(2, n-2)
    elif i == 3:
        dp[n][i] = endsWith(1, n-3) + endsWith(2, n-3) + endsWith(3, n-3)
    return dp[n][i]

def solve(n):
    sum_ = 0
    for i in range(1, 4):
        sum_ += endsWith(i, n)
    return sum_

def main(f = None):
    global dp
    init(f)
    t = int(input().strip())
    dp = [[None for _ in range(4)] for _ in range(10001)]
    dp[0][1] = 0
    dp[0][2] = 0
    dp[0][3] = 0
    dp[1][1] = 1
    dp[1][2] = 0
    dp[1][3] = 0
    dp[2][1] = 1
    dp[2][2] = 1
    dp[2][3] = 0
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1
    for i in range(4, 10001):
        solve(i)

    for line in sys.stdin:
        n = int(line.strip())
        ans = solve(n)
        print(ans)
    

if __name__ == "__main__":
    main()