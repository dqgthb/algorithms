def main():
    st = "111"
    st = "341"
    #st = "001"
    arr = list(map(int, st))
    n = solve(arr)
    print(n)


def solve(arr):
    print(arr)
    if len(arr) < 2:
        return 1

    a, b, *_ = arr
    n = 0
    if a != 0:
        n += solve(arr[1:])
    if 0 < a < 3 and 10*a + b <= 26:
        n += solve(arr[2:])
    return n


if __name__ == "__main__":
    main()