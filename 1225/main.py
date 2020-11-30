import itertools
def solve(A, B):
    dA = [int(i) for i in str(A)]
    dB = [int(i) for i in str(B)]

    prod = itertools.product(dA, dB)

    return sum(i*j for i, j in prod)


def main():
    A, B = (i for i in input().split())
    ans = solve(A, B)
    print(ans)

if __name__ == "__main__":
    main()

