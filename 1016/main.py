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

class Sieve:
    def __init__(s, mi, ma):
        s.mi = mi
        s.ma = ma
        s.arr = [True for _ in range(ma-mi+1)]

        for i in range(2, 1000001):
            sqr = i*i
            q, r = divmod(mi, sqr)
            if r == 0:
                start = mi
            else:
                start = sqr * (q+1)
            for j in range(start, ma + 1, sqr):
                s.set(j, False)
    
    def get(s, n):
        return s.arr[n - s.mi]
    
    def set(s, n, v):
        s.arr[n - s.mi] = v
    
    def count(s):
        count = 0
        for i in s.arr:
            if i:
                count += 1
        return count

def main(f = None):
    init(f)
    mi, ma = (int(i) for i in input().split())
    sieve = Sieve()
    ans = sieve.count()
    print(ans)



if __name__ == "__main__":
    main()