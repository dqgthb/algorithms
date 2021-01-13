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
        s.tree = [None for _ in range(4 * s.len)]
        s._initialize(0, s.len-1, 0)

    def _initialize(s, l, r, idx):
        mid = (l + r) // 2
        if l == r:
            val = s.arr[l]
            s.tree[idx] = val
            return val
        else:
            val = s._initialize(l, mid, idx * 2 + 1) + s._initialize(mid+1, r, idx * 2 + 2)
            s.tree[idx] = val
            return val
    
    def rangeSum(s, l, r):
        return s._rangeSum(l, r, 0, s.len-1, 0)
    
    def _rangeSum(s, l, r, start, end, idx):
        if r < start or end < l:
            return 0

        if l <= start and end <= r:
            return s.tree[idx]

        mid = (start + end) // 2
        lSum = s._rangeSum(l, r, start, mid, idx * 2 + 1)
        rSum = s._rangeSum(l, r, mid+1, end, idx * 2 + 2)
        return lSum + rSum


    def update(s, loc, val):
        prev = s.arr[loc]
        s.arr[loc] = val
        delta = val - prev
        s._update(loc, delta, 0, s.len - 1, 0)


    def _update(s, loc, delta, start, end, idx):
        if loc < start or end < loc:
            return

        s.tree[idx] += delta
        if start == end:
            return
        
        mid = (start + end) // 2
        if loc <= mid:
            s._update(loc, delta, start, mid, idx * 2 + 1)
        else:
            s._update(loc, delta, mid+1, end, idx * 2 + 2)


def main(f = None):
    init(f)
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    tree = [None for _ in range(4 * len(arr))]

    s = SegTree(arr)
    for i in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            s.update(b-1, c)
        else:
            ans = s.rangeSum(b-1, c-1)
            print(ans)




if __name__ == "__main__":
    main()