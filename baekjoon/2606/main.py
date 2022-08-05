DEBUG = False
DEBUG = True

N = 0
E = 0
arr = None

import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

count = 0
visited = []
eg = []
def dfs(n):
    global count, visited, eg

    assert not visited[n], "already visited %d" % n
    count += 1
    visited[n] = True
    for i in eg[n]:
        if not visited[i]:
            dfs(i)

def main():
    global count, visited, eg
    #N = int(input())
    N = 1000
    if N == 0: print("0"); return
    E = int(input())
    visited = [False for i in range(N+1)]
    eg = [set() for _ in range(N+1)]
    for line in sys.stdin:
        a, b = (int(i) for i in line.split())
        eg[a].add(b)
        eg[b].add(a)
    dfs(1)
    print(count - 1)



if __name__ == "__main__":
    main()
