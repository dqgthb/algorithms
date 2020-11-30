import os
import sys
if os.path.exists("i"):
    sys.stdin = open("i")


def printe(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def input():
    return sys.stdin.readline()

def main():
    n = int(input())

    arr = [(l[0], l[1]) for _ in range(n) if ( l := [int(i) for i in input().split()])]

    arr.sort(key = lambda x: x[1])
    arr.sort(key = lambda x: x[0])

    for i in arr:
        print(i[0], i[1])




if __name__ == "__main__":
    main()