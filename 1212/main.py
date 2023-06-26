# Python Competitive Programming Template (updated 2023-04-07)
# Created by dqgthb
from sys import stdin, argv
from os import path


def main() -> None:
    N = int(input())

    N_ = [int(i) for i in str(N)]

    ans = ''.join(toBinary(i) for i in N_)

    ans = ans.lstrip('0')

    print('0' if ans == '' else ans)


def toBinary(x: int):

    ret = []
    while x > 0:
        x, r = divmod(x, 2)
        ret.append(r)
    ret.reverse()
    ans = ''.join(map(str, ret))

    ans = '0' * (3 - len(ans)) + ans
    return ans


if __name__ == "__main__":
    global input
    input = stdin.readline
    if len(argv) == 2:
        input = open(argv[1]).readline
    elif path.isfile("i"):
        input = open("i").readline

    main()
