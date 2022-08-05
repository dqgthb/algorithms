import os
import sys
import itertools
import collections
TEST = ''
if os.path.exists("i" + TEST):
    sys.stdin = open("i" + TEST)
if os.path.exists("a" + TEST):
    sys.stdout = open("o" + TEST, "w" + TEST)
input=sys.stdin.readline


def printe(*args,**kwargs):
    print(*args, **kwargs, file=sys.stderr)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def get_ints(): return map(int, sys.stdin.readline().strip().split())


def dfs(n):
    global N, M, eg, cc, visited

    visited[n] = True

    for i in eg[n]:
        if not visited[i]:
            dfs(i)


visited = []
cc = 0
N = M = 0
eg = []
def main():
    global N, M, eg, cc, visited
    N, M = (int(i) for i in input().split())
    eg = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    for _ in range(M):
        i, j = (int(i) for i in input().split())
        eg[i].append(j)
        eg[j].append(i)
    print(eg)

    for i in range(1, N+1):
        if not visited[i]:
            cc += 1
            dfs(i)

    print(cc)



if __name__ == "__main__":
    main()