from bisect import *
def main():
    arr = "0011112244"
    arr = list(map(int, arr))
    ans = bisectLeft(arr, 0, 0, len(arr))
    print(ans)
    ans = bisectRight(arr, 0, 0, len(arr))
    print(ans)
    ans = bisectLeft(arr, 1, 0, len(arr))
    print(ans)
    ans = bisectRight(arr, 1, 0, len(arr))
    print(ans)
    ans = bisectLeft(arr, 2, 0, len(arr))
    print(ans)
    ans = bisectRight(arr, 2, 0, len(arr))
    print(ans)
    ans = bisect_left(arr, 0)
    print(ans)
    ans = bisect_right(arr, 0)
    print(ans)
    ans = bisect_left(arr, 1)
    print(ans)
    ans = bisect_right(arr, 1)
    print(ans)
    ans = bisect_left(arr, 2)
    print(ans)
    ans = bisect_right(arr, 2)
    print(ans)
    ans = bisect_left(arr, 3)
    print(ans)
    ans = bisect_right(arr, 3)
    print(ans)


def bisectLeft(arr, val, left, right):
    if left == right:
        return left
    
    mid = (left + right)//2
    #print(mid, arr[mid])

    if val <= arr[mid]:
        return bisectLeft(arr, val, left, mid)
    else:
        return bisectLeft(arr, val, mid+1, right)

def bisectRight(arr, val, left, right):
    if left == right:
        return left
    
    mid = (left + right)//2
    #print(mid, arr[mid])

    if val >= arr[mid]:
        return bisectRight(arr, val, mid+1, right)
    else:
        return bisectRight(arr, val, left, mid)


if __name__ == "__main__":
    main()