DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")


def print_(*args):
    if DEBUG:
        print(*args)


def main():
    t = int(input().strip())
    for line in sys.stdin:
        l = line.split()
        n = int(l[0])
        st = l[1]

        ans = [c * n for c in st]
        print(''.join(ans))



if __name__ == "__main__":
    main()