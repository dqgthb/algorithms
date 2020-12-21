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

def main(f = None):
    init(f)
    N = int(input().strip())
    M = int(input().strip())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = (int(i)-1 for i in input().split())
        c += 1

        G[a].append([c, b])
    start, end = (int(i)-1 for i in input().split())
    g = Graph(G)
    dist = g.dijkstra(start)
    print(dist[end])

class Graph:
    def __init__(s, G):
        s.G = G
    
    def dijkstra(s, start):
        s.dist = [float("inf") for _ in range(len(s.G))]
        import heapq
        pq = []
        s.dist[start] = 0
        heapq.heappush(pq, (0, start))

        while pq:
            dis2Node, node = heapq.heappop(pq)

            if dis2Node > s.dist[node]:
                continue

            for disToNeighborFromNode, neighbor in s.G[node]:
                newDisFromStartToNeighbor = dis2Node + disToNeighborFromNode
                if newDisFromStartToNeighbor < s.dist[neighbor]:
                    s.dist[neighbor] = newDisFromStartToNeighbor
                    heapq.heappush(pq, [newDisFromStartToNeighbor, neighbor])

        return s.dist








if __name__ == "__main__":
    main()