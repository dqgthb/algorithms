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


class DP():
    def __init__(s, l, mat):
        s.l = l
        s.dp = [[None for _ in range(l)] for _ in range(2)]
        s.mat = mat
    
    def solve(s, i, j):
        if not 0 <= i < 2: return 0
        if not 0 <= j < s.l: return 0
        if s.dp[i][j] is not None: return s.dp[i][j]

        if j == 0: return s.mat[i][j]

        val = s.mat[i][j]
        
        diagonal = [1, 0]
        cand1 = val + s.solve(diagonal[i], j-1)
        cand2 = val + s.solve(diagonal[i], j-2)
        ret = max(cand1, cand2)
        s.dp[i][j] = ret
        return ret


def main(f = None):
    global mat
    init(f)
    t = int(input().strip())
    for _ in range(t):
        l = int(input().strip())
        mat = [list(map(int, input().split())) for _ in range(2)]
        s = DP(l, mat)
        for j in range(l):
            s.solve(0, j)
            s.solve(1, j)
        c1 = s.solve(0, l-1)
        c2 = s.solve(1, l-1)
        print(max(c1, c2))

if __name__ == "__main__":
    main()