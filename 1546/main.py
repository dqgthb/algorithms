DEBUG = False
DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(scores):
    print_(scores)
    max_ = max(scores)

    newScores = [i/max_ * 100 for i in scores]

    return sum(newScores) / len(newScores)


def main():
    while True:
        try:
            n = int(input())
            scores = [int(i) for i in input().split()]
            ans = solve(scores)
            print(ans)
        except EOFError:
            break


if __name__ == "__main__":
    main()