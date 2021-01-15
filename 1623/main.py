def main(f = None):
    init(f)

    def sol(cur, flag):
        val = cache[cur][flag]
        if val != -1: return val
        val = 0

        if flag:
            val += cost[cur]
            for nxt in tree[cur]:
                val += sol(nxt, 0)
        
        else:
            for nxt in tree[cur]:
                val += max(sol(nxt, 0), sol(nxt, 1))
        cache[cur][flag] = val
        return val

    N = int(input())
    tree = [[] for _ in range(N)]
    cost = [int(i) for i in input().split()]
    parentOf = [None] + [int(i)-1 for i in input().split()]
    for i in range(1, N):
        tree[parentOf[i]].append(i)
    del parentOf
    cache = [[-1]*2 for _ in range(N)]
    
    print(sol(0, 1), sol(0, 0))
    del cost

    def dfs(cur, flag):
        if flag:
            for nxt in tree[cur]:
                dfs(nxt, 0)
        else:
            for nxt in tree[cur]:
                if cache[nxt][0] > cache[nxt][1]:
                    dfs(nxt, 0)
                else:
                    dfs(nxt, 1)
                    lst.append(nxt+1)
    lst = [1]
    dfs(0, 1)
    lst.sort()
    pfast(*lst, -1)

    lst = []
    dfs(0, 0)
    lst.sort()
    pfast(*lst, -1)




def For(*args):
    return itertools.product(*map(range, args))

def copy2d(mat):
    return [row[:] for row in mat]

def Mat(h, w, default = None):
    return [[default for _ in range(w)] for _ in range(h)]

# CP template Version 1.005
import os
import sys
sys.setrecursionlimit(205000)

DEBUG = False

def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline

def init(f = None):
    global input
    input = sys.stdin.readline # by default
    if os.path.exists("o"): sys.stdout = open("o", "w")
    if f is not None: setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"): setStdin("in/i")
            elif os.path.isfile("i"): setStdin("i")
        elif len(sys.argv) == 2: setStdin(sys.argv[1])
        else: assert False, "Too many sys.argv: %d" % len(sys.argv)
def pfast(*args, end = "\n", sep=' '): sys.stdout.write(sep.join(map(str, args)) + end)

def parr(arr):
    for i in arr:
        print(i)

if __name__ == "__main__":
    main()