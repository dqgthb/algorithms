from heapq import heappush, heappop

def main():

    airports = []
    connectingTime = []
    with open("Hawaiian-airports.txt") as f:
        for line in f:
            airport, time = line.split()
            airports.append(airport)
            connectingTime.append(time)

    N = len(airports)
    convert = {airports[i]:i for i in range(N)}
    #print(connectingTime[convert["LNY"]])

    G = [[] for _ in range(N)]
    with open("Hawaiian-flights.txt") as f:
        for line in f:
            from_, to_, departure, arrival = line.split()
            G[convert[from_]].append((convert[to_], departure, arrival))


    S = convert("LNY")
    T = convert("LIH")
    startTime = "1347"

    pq = []
    D = [10**9 for _ in range(N)]
    heappush(pq, (0, S))

    while pq:
        dsx, x = heappop(pq)
        if dsx > D[x]:
            continue

        for y, departXY, arriveXY in G[x]:
            dxy = 0
            if dsx + dxy < D[y]:
                D[y] = dsx + dxy








def parr(A):
    for i in A:
        print(i)

if __name__ == "__main__":
    main()