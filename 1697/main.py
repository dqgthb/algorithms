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

visited = [False for _ in range(100001)]
dq = collections.deque()
K = 0
N = 0
ans = 0
def bfs(k):
    global visited, dq, ans, K, N
    if not 0 <= k <= 100000:
        return

    visited[k] = True
    dq.append((k, 0))

    while len(dq) > 0:
        curr, curStep = dq.popleft()
        if curr == N:
            ans = curStep
            return

        
        def addCand(x):
            def withinRange(x):
                return 0 <= x <= 100000
            if withinRange(x) and not visited[x]:
                visited[x] = True
                dq.append((x, curStep + 1))

        addCand(curr-1)
        addCand(curr+1)
        if curr % 2 == 0: addCand(curr//2)

def main():
    global visited, dq, ans, K, N
    N, K = (int(i) for i in input().split())
    bfs(K)
    print(ans)


if __name__ == "__main__":
    main()