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

def isPalindrom(str_):
    if str_ == str_[::-1]:
        return True
    return False

def solve(inputs):
    s = set()
    for i in inputs:

        if isPalindrom(i):
            return len(i), i

        rev = i[::-1]
        if rev in s:
            return len(i), i
        else:
            s.add(i)
    else:
        return None, None


def main(f = None):
    init(f)
    t = int(input().strip())
    inputs = []
    for line in sys.stdin:
        inputs.append(line.rstrip())

    n, ans = solve(inputs)
    if ans == None: return
    print(n, ans[len(ans)//2])

if __name__ == "__main__":
    main()