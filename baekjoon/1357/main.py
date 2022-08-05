import os
import sys
import itertools
import collections
DEBUG = False
if os.path.exists("i"):
    DEBUG = True
    sys.stdin = open("i")
if os.path.exists("a"):
    sys.stdout = open("o", "w")
input=sys.stdin.readline


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def ints(): return map(int, sys.stdin.readline().strip().split())

def main():
    if len(sys.argv) == 2:
        sys.stdin = open(sys.argv[1])
    
    a, b = input().split()
    a = ''.join(reversed(a))
    b = ''.join(reversed(b))
    a = int(a)
    b = int(b)

    c = a + b
    c = str(c)
    c = ''.join(reversed(c))
    cc = c.lstrip("0")
    print(cc)



if __name__ == "__main__":
    main()