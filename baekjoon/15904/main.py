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

def convert(bl):
    if bl == True:
        return "I love UCPC"
    return "I hate UCPC"

def solve(str_, abbrev):
    if len(abbrev) == 0:
        return True
    idx = str_.find(abbrev[0])
    if idx == -1:
        return False
    else:
        return solve(str_[idx+1:], abbrev[1:])


def main(f = None):
    init(f)
    str_ =(input().strip())
    abbrev = "UCPC"
    ans = solve(str_, abbrev)
    printStr = convert(ans)
    print(printStr)


if __name__ == "__main__":
    main()