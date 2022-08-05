import os
import sys
DEBUG = False
if os.path.exists("i"):
    DEBUG = True
    sys.stdin = open("i")


def printe(*args, **kwargs):
    import sys
    print(*args, **kwargs, file=sys.stderr)


def main():
    _ = input()
    s = set(line.strip() for line in sys.stdin)
    printe(s)
    for i in sorted(sorted(s), key = len):
        print(i)



if __name__ == "__main__":
    main()