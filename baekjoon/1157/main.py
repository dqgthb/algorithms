DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def solve(line):
    line = line.strip().upper()
    import collections as cl
    c = cl.Counter(line)
    most = c.most_common(2)
    if len(most) == 2 and most[0][1] == most[1][1]:
        return "?"
    return most[0][0]
    


def main():
    for line in sys.stdin:
        ans = solve(line)
        print(ans)

if __name__ == "__main__":
    main()