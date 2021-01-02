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

class SegTree:
    def __init__(s, arr):
        s.arr = arr
        s.len = len(arr)
        s.tree = [0] * (s.len * 4)
        s.init(0, s.len-1, 0)

    def init(s, l, r, idx):
        if l == r:
            val = s.arr[l]
            s.tree[idx] = (val, val)
            return (val, val)
        
        mid = (l + r) // 2
        min1, max1 = s.init(l, mid, idx * 2 + 1)

        min2, max2 = s.init(mid+1, r, idx * 2 + 2)
        minV = max(min1, min2)
        maxV = max(max1, max2)
        val = (minV, maxV)
        s.tree[idx] = val
        return val
    
    def getMinMax(s, l, r):
        return s._getMinMax(l, r, 0, s.len-1, 0)
    
    def _getMinMax(s, l, r, start, end, idx):
        if r < start or l > end:
            return 0

        if l <= start and end <= r:
            return s.tree[idx]
        
        mid = (start + end) // 2
        min1, max1 = s._getMax(l, r, start, mid, idx*2 + 1)
        min2, max2 = s._getMax(l, r, mid+1, end, idx*2 + 2)
        minV = min(min1, min2)
        maxV = max(max1, max2)

        return (minV, maxV)



def main(f = None):
    init(f)
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    s = SegTree(arr)
    print(s.arr)
    print(s.tree)
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        min_, max_ = s.getMinMax(a, b)
        print(min_, max_)




if __name__ == "__main__":
    main()