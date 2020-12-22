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

class HideAndCatch():
    def __init__(s, n, k):
        s.n = n
        s.k = k
        s.maxStage = 100000
        s.visited = [False for _ in range(s.maxStage+1)]
        s.parents = [None for _ in range(s.maxStage+1)]


    def bfs(s):
        dq = collections.deque()
        dq.append((s.n, 0, None))
        while dq:
            curr, time, parent = dq.popleft()
            if s.visited[curr]:
                continue
            s.visited[curr] = True
            s.parents[curr] = parent
            if curr == s.k:
                return time

            nextStep = [curr+1, curr-1, curr*2]
            for i in nextStep:
                if 0 <= i <= s.maxStage and not s.visited[i]:
                    dq.append((i, time+1, curr))
        else:
            print("answer not found!")
    def getParents(s):



def main(f = None):
    init(f)
    pass
    N, K = (int(i) for i in input().split())
    hac = HideAndCatch(N, K)
    ans = hac.bfs()
    print(ans)


if __name__ == "__main__":
    main()