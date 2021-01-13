def solve(N, F):
    N = N // 100 * 100

    for i in range(100):
        if (N + i) % F == 0:
            if i < 10:
                return "0" + str(i)
            else:
                return str(i)

def main():
    """
    N = 1000
    F = 3
    solve(N, F)

    N = 1000
    F = 4
    solve(N, F)
    """

    N = int(input())
    F = int(input())
    solve(N, F)
    # for N in range(100, 200):
    #     for F in range(1, 100):
    #         print("Answer for ", N, F)
    #         print(solve(N, F))






if __name__ == "__main__":
    main()