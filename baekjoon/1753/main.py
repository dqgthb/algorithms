import os
import sys
#from heapq import heappush, heappop
import heapq

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
        print("### DEBUG ###", end=': ')
        print(*args)


def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)

def ints(): return map(int, sys.stdin.readline().split())

def main(f = None):
    init(f)
    V, E = (int(i) for i in input().split())
    K = int(input().strip())-1
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u-1].append((w, v-1))

    D = [123456789 for _ in range(V)]
    start = K
    adjs = []
    D[start] = 0
    heapq.heappush(adjs, (0, start))

    count = 0
    while adjs:
        dprint(f"adjs is {adjs}")
        distance, currV = heapq.heappop(adjs)
        if distance > D[currV]:
            dprint(f"{distance} is larger than {D[currV]}")
            continue
        count += 1
        dprint(f"processing {distance}, {currV}")

        for edge in G[currV]:
            dprint(f"edge is {edge}")
            w, v  = edge
            Dv = D[v]
            dToV = w + distance
            if dToV < Dv:
                D[v] = dToV
                heapq.heappush(adjs, (dToV, v))
                dprint(f"{(dToV, v)} added to heapq")
        dprint("loop")

    for d in D:
        if d == 123456789:
            pfast("INF")
        else:
            pfast(d)
    print("count:", count)


if __name__ == "__main__":
    main()