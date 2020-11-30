import sys
#sys.stdin = open("i", "r")

import statistics

def solve(line):
    lst = [int(i) for i in line.split()]
    ln = lst[0]
    scores = lst[1:]

    avg = statistics.mean(scores)

    count = 0
    for i in scores:
        if i > avg:
            count += 1

    return count / ln * 100


def main():
    n = input()
    for line in sys.stdin:
        ans = solve(line)
        print("{:.3f}%".format(ans))

if __name__ == "__main__":
    main()