DEBUG = False
import sys
#DEBUG = True

if DEBUG:
    sys.stdin = open("i", "r")

def print_(*arg):
    if DEBUG:
        print(*arg)


def solve(line):
    a, b, c = (int(i) for i in line.split())

    sums = [0 for _ in range(100)]

    import itertools
    for i, j, k in itertools.product(range(1, a+1), range(1, b+1), range(1, c+1)):
        sums[i + j + k] += 1

    print_(sums)

    max_ = 0
    idx = 0
    for i, e in enumerate(sums):
        if e > max_ :
            max_ = e
            idx = i
    return idx



def main():
    for line in sys.stdin:
        ans = solve(line)
        print(ans)

if __name__ == "__main__":
    main()