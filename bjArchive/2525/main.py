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

def solve(A, B, C):
    import datetime
    now = datetime.datetime(100, 1, 1, A, B, 0)
    after = now + datetime.timedelta(0, C * 60)
    return ' '.join(map(str, (after.hour, after.minute)))


def main(f = None):
    init(f)
    A, B = (int(i) for i in input().split())
    C = int(input().strip())
    ans = solve(A, B, C)
    print(ans)

if __name__ == "__main__":
    main()