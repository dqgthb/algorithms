import sys
input = sys.stdin.readline


class Freq:
    def __init__(self, value, frequency):
        self.v = value
        self.f = frequency


def main(f=None):


    N = int(input())
    arr = [int(input()) for _ in range(N)]

    stack = []
    cnt = 0

    for i in arr:

        while stack and stack[-1].v < i:
            cnt += stack.pop().f

        if stack:
            last = stack[-1]
            if last.v == i:
                cnt += last.f
                if len(stack) > 1:
                    cnt += 1
                last.f += 1
                continue

            else:
                cnt += 1

        stack.append(Freq(i, 1))

    print(cnt)


if __name__ == "__main__":
    main()