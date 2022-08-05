import os
import sys
import itertools
import collections

DEBUG = False
if len(sys.argv) == 1:
    if os.path.exists("i"):
        DEBUG = True
        sys.stdin = open("i")

    if os.path.exists("a"):
        sys.stdout = open("o", "w")

elif len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
else:
    assert False, "too many arguments"
input=sys.stdin.readline


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def ints(): return map(int, sys.stdin.readline().strip().split())


sieve = [i for i in range(100001)]

def solve(n):
    yak = []

    yak = [i for i in range(1, n) if n % i == 0]

    if n == sum(yak):
        print(n, "=", " + ".join(map(str, yak)))
    else:
        print(n, "is NOT perfect.")





def main():
    while True:
        i = int(input().strip())
        if i == -1:
            return
        
        solve(i)






if __name__ == "__main__":
    main()