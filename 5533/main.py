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
    t = int(input().strip())
    arr = []
    for _ in range(t):
        arr.append([int(i) for i in input().split()])
    
    tarr = list(zip(*arr))

    scores = [0 for _ in range(t)]

    import collections as col
    
    for cards in tarr:
        cnt = col.Counter(cards)
        for i, c in enumerate(cards):
            if cnt[c] == 1:
                scores[i] += c
    
    for i in scores:
        print(i)



if __name__ == "__main__":
    main()