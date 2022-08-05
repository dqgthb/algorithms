import sys
import itertools
#sys.stdin = open("i", "r")

def solve(line):
    month, day = (int(i) for i in line.split())

    lastDay = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    assert 1 <= month <= 12 and 1 <= day <= lastDay[month], "invalid input %d %d" % (month, day)

    cumulDay = list(itertools.accumulate(lastDay))

    days = 0
    days += cumulDay[month-1]
    days += day

    dayName = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    return dayName[days % 7]


def main():
    for line in sys.stdin:
        ans = solve(line)
        print(ans)

if __name__ == "__main__":
    main()