def solution(n, info):
    global points, costs
    points = []
    costs = []
    enemyPoint = 0
    for i, e in enumerate(info):
        if e > 0:
            enemyPoint += 10-i
            points.append(2*(10-i))
        else:
            points.append(10-i)
        costs.append(e+1)
    costs[0] = 0

    ans, items = solve(0, n, [])
    shots = [0] * 11
    for i in items:
        shots[i] = costs[i]
    shots[10] = n - sum(shots)


    ryan = 0
    apeach = 0
    for i in range(10):
        r = shots[i]
        a = info[i]
        if not (a == 0 and r == 0):
            if a >= r:
                apeach += (10 - i)
            else:
                ryan += (10 - i)

    #ans2, items2 = solve2(0, n, [])
    #shots2 = [0] * 11
    #for i in items:
    #    shots2[i] = costs[i]
    #shots2[10] = n - sum(shots2)

    #if shots2[10] > shots[10]:
    #    shots = shots2

    if ryan > apeach:
        return shots
    else:
        print(shots)
        return [-1]


def solve(item, n, chosen):
    if item == 11:
        return (0, chosen)

    c2, items2 = solve(item+1, n, chosen[:])
    if n >= costs[item]:
        c1, items1 = solve(item+1, n - costs[item], chosen + [item])
        if c1 + points[item] > c2:
            return c1 + points[item], items1

    return c2, items2

def solve2(item, n, chosen):
    if item == 10:
        return (0, chosen)

    c2, items2 = solve(item+1, n, chosen[:])
    if n >= costs[item]:
        c1, items1 = solve(item+1, n - costs[item], chosen + [item])
        if c1 + points[item] >= c2:
            return c1 + points[item], items1

    return c2, items2


def main():
    n = 5
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    print(solution(n, info))

    n = 1
    info = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(solution(n, info))

    n = 9
    info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
    print(solution(n, info))

    n = 10
    info = [0,0,0,0,0,0,0,0,3,4,3]
    print(solution(n, info))


if __name__ == "__main__":
    main()

