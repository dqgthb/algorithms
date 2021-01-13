import os
import sys
if os.path.exists("i"):
    sys.stdin = open("i")


def printe(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


class Member:
    def __init__(self, age, name):
        self.age = age
        self.name = name


def main():
    n = int(input())
    members = [Member(int(l[0]), l[1]) for _ in range(n) if (l := input().split())]
    members.sort(key=lambda x: x.age)

    for m in members:
        print(m.age, m.name)

if __name__ == "__main__":
    main()