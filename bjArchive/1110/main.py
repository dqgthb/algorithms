import sys
sys.stdin = open('i', 'r')

def fstsnd(n):
    assert 0 <= n <= 99
    strn: str = str(n)
    if len(strn) == 1:
        return 0, int(strn)
    return (int(i) for i in strn)

def solve(a: int):
    i: int = 0
    encountered = {}
    while True:
        fst, snd = fstsnd(a)
        sum_ = int(str(snd) + str((fst + snd) % 10))
        if sum_ in encountered:
            return i - encountered[sum_]
        else:
            encountered[sum_] = i
            i += 1
            a = sum_

def main():
    inp: int = int(input())
    assert 0 <= inp <= 99, "wrong input range"

    ans = solve(inp)

    print(ans)


if __name__ == "__main__":
    main()