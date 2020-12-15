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
    msg = input().strip()

    happy = 0
    sad = 0
    for i in range(len(msg)-2):
        str_ = msg[i:i+3]
        if str_ == ":-)":
            happy += 1
        elif str_ == ":-(":
            sad += 1
    
    if happy == 0 and sad == 0:
        print("none")
    elif happy == sad:
        print("unsure")
    elif happy > sad:
        print("happy")
    else:
        print("sad")



if __name__ == "__main__":
    main()