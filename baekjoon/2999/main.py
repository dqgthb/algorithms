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
    str_ = input().strip()
    l = len(str_)
    import math
    R = 0
    for i in range(int(math.sqrt(l)), 0, -1):
        if l % i == 0:
            R = i
            break
    assert R != 0
    C = l // R

    arr = [[None for _ in range(C)] for _ in range(R)]
    idx = 0
    for j in range(C):
        for i in range(R):
            arr[i][j] = str_[idx]
            idx += 1

    res = [None for _ in range(len(str_))]
    idx = 0
    for i in range(R):
        for j in range(C):
            res[idx] = arr[i][j]
            idx += 1
    print(''.join(res))





if __name__ == "__main__":
    main()