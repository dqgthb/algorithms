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


def ints(): return map(int, sys.stdin.readline().strip().split())


count = 0
def testCase(m, n, k):
    global count
    mat = [[False for i in range(m)] for i in range(n)]

    for _ in range(k):
        j, i = ints()
        mat[i][j] = True

    for i in range(n):
        for j in range(m):
            if mat[i][j] == True:
                count += 1
                dfs(mat, i, j, m, n)
    print(count)
    count = 0

def dfs(mat, i, j, m, n):
    if not 0 <= i < n: return
    if not 0 <= j < m: return
    if not mat[i][j]: return

    mat[i][j] = False
    dfs(mat, i-1, j, m, n)
    dfs(mat, i+1, j, m, n)
    dfs(mat, i, j-1, m, n)
    dfs(mat, i, j+1, m, n)

def main():
    t = int(input().strip())
    for _ in range(t):
        M, N, K = ints()
        testCase(M, N, K)



if __name__ == "__main__":
    main()