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

class eratosthenessSieve:
    def __init__(s, n):
        s.n = n
        s.arr = [True for _ in range(n+1)]
        for num in range(2, n):
            for i in range(num*2, n, num):
                s.arr[i] = False

def main(f = None):
    init(f)
    et = eratosthenessSieve(123456 * 2)

    print(et.arr[0:100])
    while False:
        n = int(input().strip())
        if n == 0: return

        arr = et.arr
        count = 0
        for i in range(n+1, 2*n+1):
            if arr[i]:
                count += 1
        
        print(count)

if __name__ == "__main__":
    main()