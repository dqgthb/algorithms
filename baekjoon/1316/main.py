DEBUG = False
#DEBUG = True
import sys
if DEBUG:
    sys.stdin = open("i", "r")
def print_(*args):
    if DEBUG:
        print(*args)

def isGroup(str_):
    occurred = set()
    prev = None
    for c in str_:
        if c != prev:
            if c in occurred:
                return False
            occurred.add(c)
            prev = c
    return True
    

def main():
    t = int(input())
    count = 0
    for _ in range(t):
        if isGroup(input().strip()):
            count += 1
    print(count)

if __name__ == "__main__":
    main()