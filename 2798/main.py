import os
import sys
DEBUG = False
if os.path.exists("i"):
    DEBUG = True
    sys.stdin = open("i2")


def printe(*args, **kwargs):
    import sys
    print(*args, **kwargs, file=sys.stderr)


def solve(N, line):
    arr = [int(i) for i in line.split()]

    ln = len(arr)
    max_ = 0
    for i in range(ln - 2):
        for j in range(i+1, ln - 1):
            for k in range(j+1,ln):
                e = arr[i] + arr[j] + arr[k]
                if max_ < e <= N:
                    max_ = e
    return max_


def main():
    for line in sys.stdin:
        _, N = (int(i) for i in line.split())
        line = sys.stdin.readline()
        ans = solve(N, line.strip())
        print(ans)


if __name__ == "__main__":
    main()