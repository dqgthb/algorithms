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
        import math
        size = 2 ** math.ceil(math.log(s.len, 2))
        s.tree = [None] * (size * 2)
        s.treeSize = len(s.tree)
        #s.tree[s.treeSize-s.len: s.treeSize] = arr[:]
        #s.initIter()
        s.init(0, s.len-1, 0)

    def initIter(s):
        for i in range(s.treeSize-s.len-1, -1, -1):
            s.tree[i] = i
        print(s.tree)



    def init(s, l, r, idx):
        if l == r:
            val = s.arr[l]
            s.tree[idx] = val
            return val
        
        mid = (l + r) // 2
        min1 = s.init(l, mid, idx * 2 + 1)

        min2 = s.init(mid+1, r, idx * 2 + 2)
        minV = min(min1, min2)
        val = minV
        s.tree[idx] = val
        return val
    
    def getMin(s, l, r):
        return s._getMin(l, r, 0, s.len-1, 0)
    
    def _getMin(s, l, r, start, end, idx):
        if r < start or l > end:
            return sys.maxsize

        if l <= start and end <= r:
            return s.tree[idx]
        
        mid = (start + end) // 2
        min1 = s._getMin(l, r, start, mid, idx*2 + 1)
        min2 = s._getMin(l, r, mid+1, end, idx*2 + 2)
        minV = min(min1, min2)

        return minV



def main(f = None):
    init(f)
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    s = SegTree(arr)
    write = sys.stdout.write
    #answerList = []
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        ans = s.getMin(a, b)
        write(str(ans) + '\n')
        #answerList.append(str(ans)+'\n')
    #sys.stdout.writelines(answerList)


if __name__ == "__main__":
    main()