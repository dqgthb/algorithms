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

def gen():
    for i in itertools.count(start=1):
        counter = 0
        while counter < i:
            yield i
            counter += 1

def main(f = None):
    init()
    A, B = (int(i)-1 for i in input().split())
    obj = gen()
    for _ in range(A):
        next(obj)

    sum_ = 0
    for _ in range(A, B+1):
        sum_ += next(obj)
    print(sum_)

if __name__ == "__main__":
    main()