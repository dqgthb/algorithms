import os
import sys
import itertools
import collections
DEBUG = False
if os.path.exists("i"):
    DEBUG = True
    sys.stdin = open("i")
if os.path.exists("a"):
    sys.stdout = open("o", "w")
#input=sys.stdin.readline


def dprint(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def ints(): return map(int, sys.stdin.readline().strip().split())


vDFS = []
vBFS = []
seqDFS = []
seqBFS = []
N = 0
M = 0
V = 0


def main():
    global vDFS, vBFS, N, M, V, seqDFS, seqBFS
    N, M, V = (int(i) for i in input().split())
    eg = [[] for _ in range(N+1)]
    for _ in range(M):
        from_, to = (int(i) for i in input().split())
        eg[from_].append(to)
        eg[to].append(from_)
    
    for l in eg:
        l.sort()

    vDFS = [False for _ in range(N+1)]
    vBFS = [False for _ in range(N+1)]

    dfs(eg, V)
    print(' '.join(map(str, seqDFS)))

    bfs(eg, V)
    print(' '.join(map(str, seqBFS)))





def dfs(eg, start):
    global vDFS, vBFS, N, M, V, seqBFS, seqDFS

    if vDFS[start]:
        return
    else:
        vDFS[start] = True

    seqDFS.append(start)

    for v in eg[start]:
        dfs(eg, v)

def bfs(eg, start):
    global vDFS, vBFS, N, M, V, seqBFS, seqDFS

    import collections
    dq = collections.deque()

    dq.append(start)

    while len(dq) > 0:
        v = dq.popleft()

        if vBFS[v]:
            continue

        vBFS[v] = True
        seqBFS.append(v)

        for node in eg[v]:
            dq.append(node)




if __name__ == "__main__":
    main()
    if os.path.exists("i2"):
        sys.stdin = open("i2")
        main()
    if os.path.exists("i3"):
        sys.stdin = open("i3")
        main()