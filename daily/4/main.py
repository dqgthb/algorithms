def main():
    arr = [1, 2, 0]
    #arr = [8, 2, 3, 4, 5, 7, 1]
    #arr = [2, 3, 7, 6, 8, -1, -10, 15]
    #arr = [3, 4, -1, 1]
    #arr = [2, 3, -7, 6, 8, 1, -10, 15]
    #arr = [1, 1, 0, -1, -2]
    arr = [5, 4, 3, 1]

    numOfPos = pushNegToBack(arr)

    for i in range(numOfPos):
        e = arr[i]
        if e < 0:
            e = -e
        if 0 <= e < numOfPos:
            if arr[e-1] > 0:
                arr[e-1] = -arr[e-1]

    for i in range(numOfPos):
        e = arr[i]
        if e > 0:
            print(i+1)
            return


def pushNegToBack(arr):
    l = 0
    r = len(arr)
    while l < r:
        if arr[l] <= 0:
            r -= 1
            arr[l], arr[r] = arr[r], arr[l]
        else:
            l += 1
    return l


if __name__ == "__main__":
    main()