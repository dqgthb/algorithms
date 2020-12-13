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
    R, C, ZR, ZC = (int(i) for i in input().split())
    mat = [list(input().strip()) for _ in range(R)]
    
    exp = [[None for _ in range(C * ZC)] for _ in range(R * ZR)]

    for i in range(R):
        for j in range(C):
            expandDot(exp, mat, i, j, ZC, ZR)
    
    for i in exp:
        print(''.join(i))

def expandDot(exp, arr, i, j, ZC, ZR):
    dot = arr[i][j]

    startR = i * ZR
    startC = j * ZC

    for r in range(ZR):
        for c in range(ZC):
            exp[startR + r][startC + c] = dot






if __name__ == "__main__":
    main()