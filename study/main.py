import requests

def main():
    global solved, cnt, totalChecks
    cnt = 0
    totalChecks = 0
    with open("i") as f:
        line = f.readline()
        arr = list(map(int, line.split()))
        solved = set(arr)

        inputProblems = """2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 11719, 11720, 11721, 2741, 2742, 2739, 1924, 8393, 10818, 2438, 2439, 2440, 2441, 2442, 2445, 2522, 2446, 10991, 10992"""
        inputProblems = process(inputProblems)
        check(inputProblems, "input")

        dp = """1463, 11726, 11727, 9095, 10844, 11057, 2193, 9465, 2156, 11053, 11055, 11722, 11054, 1912, 2579, 1699, 2133, 9461, 2225, 2011, 11052"""
        dp = process(dp)
        check(dp, "dp")

        thisthat = '2751, 11650, 11651, 10814, 10825, 10989, 11652, 11004, 10828, 9012, 10799, 10845, 10866, 10808, 10809, 10820, 2743, 11655, 10824, 11656, 1406, 1158, 1168, 10430, 2609, 1934, 1850, 9613, 11005, 2745, 1373, 1212, 2089, 11576, 1978, 1929, 6588, 11653, 10872, 1676, 2004'
        thisthat = process(thisthat)
        check(thisthat, "thisthat")

        graph = "1260, 11724, 1707, 10451, 2331, 9466, 2667, 4963, 7576, 2178, 2146, 1991, 11725, 1167, 1967"
        graph = process(graph)
        check(graph, "graph")

        binarySearch = "1654, 2805, 2110, 10815, 10816, 11662"
        binarySearch = process(binarySearch)
        check(binarySearch, "binarySearch")

        divideConquer = "11728, 1780, 11729, 1992, 2447, 2448, 1517, 2261"
        divideConquer = process(divideConquer)
        check(divideConquer, "divide and conquer")

        greedy = "11047, 2875, 10610, 1783, 1931, 11399, 2873, 1744"
        greedy = process(greedy)
        check(greedy, "greedy")

        exhaustiveSearch = "1476, 1107, 1451, 9095, 10819, 10971, 1697, 1963, 9019, 1525, 2251, 2186, 3108, 5014, 1759, 2580, 1987, 6603, 1182, 2003, 1806, 1644, 1261, 1208, 7453, 2632, 2143"
        exhaustiveSearch = process(exhaustiveSearch)
        check(exhaustiveSearch, "exhaustive")

    print("total problems:", totalChecks)
    print("unsolved:", cnt)


def process(text):
    return [int(i) for i in text.split(", ")]


tier = "BSGPDR"

def check(list_, topic = ""):
    url = "https://solved.ac/api/v3/problem/lookup"
    headers = {"Content-Type": "application/json"}

    global cnt, totalChecks
    print(topic)
    for problem in list_:
        totalChecks += 1
        if problem not in solved:
            querystring = {"problemIds":str(problem)}
            response = requests.request("GET", url, headers=headers, params=querystring)
            level = response.json()[0]["level"]
            q, r = divmod(level-1, 5)
            print(problem, tier[q], 5-r, end='/')
            cnt += 1
    print()


if __name__ == "__main__":
    main()