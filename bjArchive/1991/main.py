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

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def main(f = None):
    init(f)
    pass
    N = int(input().strip())
    import string
    abc = string.ascii_uppercase[:N]
    loc = {c:None for c in abc}
    loc['.'] = None
    for c in abc:
        loc[c] = Node(c)

    for _ in range(N):
        p, l, r = input().split()
        loc[p].left = loc[l]
        loc[p].right = loc[r]

    root = loc['A']
    printTreePre(root)
    print()
    printTreeMid(root)
    print()
    printTreePost(root)
    print()

def printTreePost(node):
    if node is None: return
    printTreePost(node.left)
    printTreePost(node.right)
    print(node.val, end='')

def printTreeMid(node):
    if node is None: return
    printTreeMid(node.left)
    print(node.val, end='')
    printTreeMid(node.right)

def printTreePre(node):
    if node is None: return
    print(node.val, end='')
    printTreePre(node.left)
    printTreePre(node.right)


if __name__ == "__main__":
    main()
