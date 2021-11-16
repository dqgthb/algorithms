# CP template Version 1.006
import os
import sys

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    N, A ,B, C, D = map(int, input().split())

    if A * D > C * B:
        A, B, C, D = C, D, A, B

    q, r = divmod(N, C)
    cost = ((N-1) // C + 1) * D
    for i in range(A+1):
        if q < i:
            break
        newCost =  (q - i) * D + ((C * i + r - 1) // A + 1) * B
        if newCost < cost:
            cost = newCost
    print(cost)


    # ######## INPUT AREA END ############


# TEMPLATE ###############################


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


def init(f=None):
    global input
    input = sys.stdin.readline  # by default
    if os.path.exists("o"):
        sys.stdout = open("o", "w")
    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"):
                setStdin("in/i")
            elif os.path.isfile("i"):
                setStdin("i")
        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])
        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)


def pr(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()