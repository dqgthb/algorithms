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

def solve(n, arr):
    global kinds
    if n == 0:
        kinds.append(arr)
        return

    for i in range(1, 4):
        if n >= i:
            newArr = arr[:]
            newArr.append(i)
            solve(n-i, newArr)

def main(f = None):
    global kinds
    init(f)
    kinds = []
    n, k = (int(i) for i in input().split())
    solve(n, [])

    k = k-1
    if k >= len(kinds):
        print(-1)
        return
    arr = kinds[k]
    s = '+'.join(map(str, arr))
    print(s)


if __name__ == "__main__":
    main()