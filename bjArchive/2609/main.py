import os
import sys
if os.path.exists("i"):
    sys.stdin = open("i")


def printe(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

def maxmin(arr):
    max_ = min_ = arr[0]
    for i in arr:
        if max_ < i:
            max_ = i
        if i < min_:
            min_ = i
    return max_, min_

def mygcd(a, b):
    if b == 0: return a
    import math
    # return math.gcd(a, b)

    ma, mi = maxmin((a, b))
    return mygcd(mi, ma % mi)


def solve(line):
    a, b = (int(i) for i in line.split())
    gcd_ = mygcd(a, b)
    print(gcd_)
    print(a * b // gcd_)


def main():
    for line in sys.stdin:
        solve(line.strip())
        break


if __name__ == "__main__":
    main()