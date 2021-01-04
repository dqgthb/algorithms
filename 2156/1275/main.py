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
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    st = SegTree(arr)
    for _ in range(Q):
        x, y, a, b = map(lambda x:int(x)-1, input().split())
        if x > y: x,y = y,x
        ans = st.query(x, y)
        print(ans)
        st.update(a, b+1)


class SegTree:
    def __init__(s, arr):
        s.a = arr
        n = len(arr)
        tree = [None] * (2 * n)
        tree[n:] = arr
        
        for i in range(n-1, 0, -1):
            tree[i] = tree[2*i] + tree[2*i + 1]
        s.n = n
        s.tree = tree

    def update(s, idx, val):
        t = s.tree
        n = s.n
        idx += n
        t[idx] = val

        while idx > 1:
            idx >>= 1
            t[idx] = t[2*idx] + t[2*idx + 1]

    def query(s, l, r):
        n = s.n
        t = s.tree
        l += n
        r += n
        i = 0
        while l <= r:
            if l & 1:
                i += t[l]
                l += 1
            
            if not r & 1:
                r -= 1
                i += t[r]
            l >>= 1
            r += 1
            r >>= 1
        return i

if __name__ == "__main__":
    main()