from heapq import heappop, heappush
import sys
import os


def main() -> None:

    openFile = open("input.txt") if os.path.isfile("i3.txt") else sys.stdin
    with openFile as f:
        global N, M, K, X
        N, M, K, X = map(int, f.readline().split())
        X -= 1

        G = [[] for _ in range(N)]
        for _ in range(M):
            A, B = map(int, f.readline().split())
            A -= 1
            B -= 1

            G[A].append(B)

        shortestDistances = dijkstra(G, X)

        # if sum(1 for i in shortestDistances if i == K) == 0:
        if K not in shortestDistances:
            print(-1)
        else:
            ans = (i + 1 for i, e in enumerate(shortestDistances) if e == K)
            print('\n'.join(map(str, ans)))


def dijkstra(G, startingCity):

    distanceFromStartingCitySoFar = [10**9] * N  # max init
    distanceFromStartingCitySoFar[startingCity] = 0

    # priorityQueue containing (distanceFromSToX, cityX)
    pq = [(0, startingCity)]

    while pq:
        shortestDistanceToX, cityX = heappop(pq)

        if shortestDistanceToX > distanceFromStartingCitySoFar[cityX]:
            continue

        # cityX's neighboring cities are named cityY
        for cityY in G[cityX]:
            distanceFromCityS = distanceFromStartingCitySoFar[cityX] + 1
            if distanceFromCityS < distanceFromStartingCitySoFar[cityY]:
                distanceFromStartingCitySoFar[cityY] = distanceFromCityS
                heappush(pq, (distanceFromCityS, cityY))
    return distanceFromStartingCitySoFar


if __name__ == "__main__":
    main()
