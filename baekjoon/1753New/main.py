import sys
from heapq import heappush, heappop

def main(f=None):
    input = sys.stdin.readline

    V, E = map(int, input().split())
    K = int(input())
    G = [[] for _ in range(V)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1

        G[a].append((b, c))


    INF = 10**9
    D = [INF] * V
    vis = [False] * V
    S = K-1
    D[S] = 0
    pq = [(0, S)]
    cnt = 0

    while pq:
        dsx, x = heappop(pq)
        vis[x] = True

        for y, dxy in G[x]:
            if vis[y]:
                continue
            dsy = dsx + dxy
            if dsy < D[y]:
                D[y] = dsy
                heappush(pq, (dsy, y))

    sys.stdout.write('\n'.join(str(i) if i != INF else "INF" for i in D))


if __name__ == "__main__":
    main()