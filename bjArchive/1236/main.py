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
    N, M = (int(i) for i in input().split())
    rows = [False for _ in range(N)]
    cols = [False for _ in range(M)]

    arr = [list(input().strip()) for _ in range(N)]
    
    import itertools
    for i,j in itertools.product(range(N), range(M)):
        if arr[i][j] == 'X':
            rows[i] = True
            cols[j] = True
    
    rowsMissing = sum(1 for i in rows if i == False)
    colsMissing = sum(1 for i in cols if i == False)

    print(max(rowsMissing, colsMissing))


if __name__ == "__main__":
    main()