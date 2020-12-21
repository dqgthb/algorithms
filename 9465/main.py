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

def solve():
    

class DP():
    def __init__(s, l, mat):
        s.l = l
        s.dp = [[None for _ in range(l)] for _ in range(2)]
        s.mat = mat
    
    def solve(s, i, j):
        assert 0 <= i < 2
        assert 0 <= j < s.l
        if s.dp[i][j] is not None: return s.dp[i][j]

        if j == 0: pass
        if j == s.l - 1: pass

        val = s.dp[i][j]

        if i == 0:
            cand1 = val + s.solve(1, j-1)
            cand2 = val + s.solve(1, j-2)


def main(f = None):
    global mat
    init(f)
    t = int(input().strip())
    for _ in range(t):
        l = int(input().strip())
        mat = [list(map(int, input().split())) for _ in range(2)]
        s = DP(l, mat)
        ans = solve()

if __name__ == "__main__":
    main()