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

def convertGtoF(G):
    Gs = "ABCDF"
    Fs = [4.0, 3.0, 2.0, 1.0, 0.0]

    GtoF = {i:j for i, j in zip(Gs, Fs)}
    F = GtoF[G[0]]
    if G == 'F':
        return 0.0

    if G[1] == '+':
        F += 0.3
    elif G[1] == '-':
        F -= 0.3
    elif G[1] != '0':
        raise "wrong input"
    return F

def main(f = None):
    init(f)
    n = int(input().strip())
    crs = [list(input().split()) for _ in range(n)]
    for i in range(len(crs)):
        credit = crs[i][1]
        crs[i][1] = int(credit)
        F = crs[i][2]
        crs[i][2] = convertGtoF(F)
    
    sumCredit = 0
    earned = 0

    for cr in crs:
        sumCredit += cr[1]
        earned += cr[1] * cr[2]
    
    cgpa = earned / sumCredit
    cgpa += 0.00000000001
    print("{:0.2f}".format(cgpa))


if __name__ == "__main__":
    main()