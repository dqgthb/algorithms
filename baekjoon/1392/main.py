DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    pass

def main():
    N, Q = (int(i) for i in input().split())
    times = [int(input()) for _ in range(N)]

    timeLine = [None for _ in range(sum(times))]

    idx = 0
    for i, time in enumerate(times):
        note = i + 1

        for _ in range(time):
            timeLine[idx] = note
            idx += 1

    questions = [int(input()) for _ in range(Q)]

    for i in questions:
        print(timeLine[i])


if __name__ == "__main__":
    main()