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
<<<<<<< HEAD
    
=======

>>>>>>> a3990db11e4cd5f0fbca4b284db3c35d71770137
    mat = [list(map(int, (i for i in input().strip()))) for _ in range(n)]
    for i in mat:
        print(i)

<<<<<<< HEAD

=======
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        if mat[i][0] == 1:
            dp[i][0] = 1
    
    for j in range(m):
        if mat[0][j] == 1:
            dp[0][j] = 1
        
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j]

    for i in dp:
        print(i)
    
>>>>>>> a3990db11e4cd5f0fbca4b284db3c35d71770137

if __name__ == "__main__":
    main()