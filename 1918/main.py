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
    exp = input().strip()
    res = []
    stack = []
    op = {'+':2, '-': 2, '*': 3, '/': 3, '(':0}

    for c in exp:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while (d := stack.pop()) != '(':
                res.append(d)
        elif c in op:
            while stack and op[stack[-1]] > op[c]:
                res.append(stack.pop())
            stack.append(c)
        else:
            res.append(c)
    res.extend(stack)
    
    print(''.join(res))


if __name__ == "__main__":
    main()