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

class eratosthenesSieve:
    def __init__(s, N):
        s.N = N
        s.primes = None
        s.arr = [True for _ in range(N+1)]
        s.arr[0] = False
        s.arr[1] = False
        for i in range(2, N-1):
            for j in range(2 * i, N+1, i):
                s.arr[j] = False
    
    def isPrime(s, n):
        return s.arr[n]
    
    def getPrimes(s):
        if s.primes is not None:
            return s.primes

        s.primes = [i for i, e in enumerate(s.arr) if e]
        return s.primes


def main(f = None):
    init(f)
    N = int(input().strip())
    es = eratosthenesSieve(N)
    print(es.getPrimes())

if __name__ == "__main__":
    main()