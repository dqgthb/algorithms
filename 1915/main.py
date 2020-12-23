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
    n, m = map(int, input().split())
    
    mat = [list(map(int, (i for i in input().strip()))) for _ in range(n)]

    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        if mat[i][0] == 1:
            dp[i][0] = 1

    for i in range(m):
        if mat[0][i] == 1:
            dp[0][i] = 1

    max_ = 0
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] == 1:
                dia = dp[i-1][j-1]
                up = dp[i-1][j]
                down = dp[i][j-1]
                ret = min((dia, up, down))+1
                dp[i][j] = ret
                if ret > max_:
                    max_ = ret
    
    print(max_**2)



if __name__ == "__main__":
    main()