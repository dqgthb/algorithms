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

def solve(n):
    global dp
    if dp[n] is not None:
        return dp[n]
    
    if n == 0:
        return s[0]
    if n == 1:
        return s[0] + s[1]
    if n == 2:
        return s[2] + max(s[0], s[1])
    
    c1 = solve(n-2)
    c2 = solve(n-3) + s[n-1]
    dp[n] = s[n] + max(c1, c2)
    return dp[n]

def main(f = None):
    init(f)
    N = int(input().strip())

    global s
    s = [int(input()) for _ in range(N)]
    global dp
    dp = [None for _ in range(N)]

    for i in range(N-1):
        solve(i)
    ans = solve(N-1)
    print(ans)

if __name__ == "__main__":
    main()