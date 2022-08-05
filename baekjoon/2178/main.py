import os
import sys
import itertools
import collections

DEBUG = False


visited = []
#count = []
mat = []
dq = []

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

def solve(mat, start, end):
    global dq

    dq = collections.deque()
    dq.append(start)
    x, y = start
    X, Y = end

    while len(dq) > 0:
        curr = dq.popleft()
        x, y = curr
        cnt = visited[x][y]

        if curr == end:
            return cnt

        up = (x, y-1)
        down = (x, y+1)
        left = (x-1, y)
        right = (x+1, y)

        directions = (up, down, left, right)
        for d in directions:
            x, y = d
            if 0 <= x <= X and 0 <= y <= Y:
                if mat[x][y] and visited[x][y] is None:
                    dq.append(d)
                    visited[x][y] = cnt + 1
            #addToQ(X, Y, d, steps = cnt + 1)

def addToQ(X, Y, futureStep, steps = 0):
    global count
    global dq
    x, y = futureStep
    if 0 <= x <= X and 0 <= y <= Y:
        if mat[x][y] and visited[x][y] is None:
            dq.append(futureStep)
            count[x][y] = steps



def main(f = None):
    global visited
    global mat
    init(f)
    N, M = (int(i) for i in input().split())
    mat = [[True if i == "1" else False for i in input().strip()] for _ in range(N)]
    visited =  [[None for __ in range(M)] for _ in range(N)]
    start = (0, 0)
    visited[0][0] = 0
    end = (N-1, M-1)

    ans = solve(mat, start, end)
    print(ans + 1)


if __name__ == "__main__":
    main()