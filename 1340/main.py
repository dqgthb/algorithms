import os
import sys
import itertools
import collections

DEBUG = False

def setStdin(f):
    global DEBUG
    global input
    DEBUG = True
    sys.stdin = open(f)
    input=sys.stdin.readline

def init(f = None):
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

def dprint(*args):
    if DEBUG:
        print(*args)

def pfast(*args, end = "\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)

def ints(): return map(int, sys.stdin.readline().rstrip().split())

def main(f = None):
    init(f)
    Month, DD, YYYY, HHMM = input().split()
    import calendar
    monthStr2Num = {month:index for index, month in enumerate(calendar.month_name) if month}
    monthNum = monthStr2Num[Month]
    DD = int(DD[0:len(DD)-1])
    YYYY = int(YYYY)
    HH, MM = (int(i) for i in HHMM.split(":"))

    import datetime
    today = datetime.datetime(YYYY, monthNum, DD, HH, MM)
    dayOfYear = today.timetuple().tm_yday - 1
    minutes = dayOfYear * 24 * 60 + HH * 60 + MM

    def isLeapYear(year):
        return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

    daysPerYear = 365 if not isLeapYear(YYYY) else 366
    minutesPerYear = daysPerYear * 24 * 60

    print(minutes / minutesPerYear * 100)




if __name__ == "__main__":
    main()