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

class DP:
    def __init__(s, A):
        s.N = len(A)
        s.A = A
        s.dp()

    
    def dp(s):
        A = s.A
        dpi = [0 for _ in range(s.N)]
        dpd = [0 for _ in range(s.N)]

        for i in range(1, s.N):
            for j in range(i-1, -1, -1):
                if A[i] > A[j]:
                    if dpi[i] <= dpi[j]:
                        dpi[i] = dpi[j] + 1
        
        for i in range(s.N-1, -1, -1):
            for j in range(i+1, s.N):
                if A[i] > A[j]:
                    if dpd[i] <= dpd[j]:
                        dpd[i] = dpd[j] + 1
        s.dpi = dpi
        s.dpd = dpd
        s.sum_ = [i+j for i, j in zip(dpi, dpd)]




def main(f = None):
    init(f)
    N = int(input().strip())
    A = [int(i) for i in input().split()]

    dp = DP(A)
    print(max(dp.sum_) + 1)

if __name__ == "__main__":
    main()