from heapq import heappush, heappop
from datetime import datetime, timedelta

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
            from_, to_, depart, arrive = line.split()

            if int(depart) >= 2400:
                depart = "00" + str(depart)[2:]

            if int(arrive) >= 2400:
                arrive = "00" + str(arrive)[2:]

            departT = datetime.strptime(depart, "%H%M")
            arriveT = datetime.strptime(arrive, "%H%M")
            timeDelta = arriveT - departT
            print(departT, arriveT)
            print(timeDelta)
            minutes = timeDelta.seconds // 60
            if timeDelta.days < 0:
                print(minutes)
                minutes += 60 * 24
            print(minutes)
            G[convert[from_]].append((convert[to_], timeDelta.seconds // 60))


    S = convert["LNY"]
    T = convert["LIH"]
    # startTime = "1347"

    pq = []
    D = [10**9 for _ in range(N)]
    P = [None for _ in range(N)]
    D[S] = 0
    heappush(pq, (0, S))

    while pq:
        dsx, x = heappop(pq)
        if dsx > D[x]:
            continue

        for y, dxy in G[x]:
            dsy = dsx + dxy
            if dsy < D[y]:
                D[y] = dsy
                P[y] = x
                heappush(pq, (dsy, y))

    print(D)
    print(P)


def parr(A):
    for i in A:
        print(i)

if __name__ == "__main__":
    main()