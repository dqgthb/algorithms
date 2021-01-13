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
    r, c = (int(i) for i in input().split())
    
    mat = [list(input().strip()) for _ in range(r)]
    
    card = [[None for _ in range(c * 2)] for _ in range(r * 2)]

    for i in range(r):
        for j in range(c):
            card[i][j] = mat[i][j]
    
    for i in mat:
        i.reverse()

    for i in range(r):
        for j in range(c):
            card[i][j+c] = mat[i][j]
    
    mat.reverse()

    for i in range(r):
        for j in range(c):
            card[i+r][j+c] = mat[i][j]
    
    for i in mat:
        i.reverse()

    for i in range(r):
        for j in range(c):
            card[i+r][j] = mat[i][j]
    
    a, b = (int(i)-1 for i in input().split())

    error = '#'
    if card[a][b] == '#': error = '.'
    
    card[a][b] = error

    for i in card:
        print(''.join(i))

if __name__ == "__main__":
    main()