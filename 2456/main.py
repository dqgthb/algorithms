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
    t = int(input().strip())
    inputs = [tuple(int(i) for i in input().split()) for _ in range(t)]
    votes = list(zip(*inputs))

    import collections
    cntrs = []
    for i, v in enumerate(votes):
        cntrs.append(collections.Counter(v))
    items = [[i[1] for i in sorted(cntr.items(), reverse=True)] for cntr in cntrs]

    stats = [(sum(e), *items[i], i) for i, e in enumerate(votes)]
    stats.sort(reverse=True)

    if stats[0][:-1] == stats[1][:-1]:
        winner = 0
    else:
        winner = stats[0][-1] + 1
    print(winner, stats[0][0])


if __name__ == "__main__":
    main()