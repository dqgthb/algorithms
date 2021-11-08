# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False

class Node:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None


def main(f=None):
    init(f)
    sys.setrecursionlimit(20000)
    # ######## INPUT AREA BEGIN ##########

    root = None
    for line in sys.stdin:
        x = int(line)
        root = insert(root, x)
    printTree(root)


    # ######## INPUT AREA END ############


def printTree(node):
    if node is None:
        return
    printTree(node.left)
    printTree(node.right)
    print(node.n)


def insert(node, val):
    if node is None:
        return Node(val)

    cn = node.n
    if val < cn:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node


# TEMPLATE ###############################


enu = enumerate


def For(*args):
    return product(*map(range, args))


def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]


def nDim(*args, default=None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default=default) for _ in range(args[0])]


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


def init(f=None):
    global input
    input = sys.stdin.readline  # by default
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


def pr(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()