from collections import Counter


def solution(A):
    counter = Counter(A)

    ans = []
    for k, v in counter.items():
        if v > 1:
            ans.append((k, v))

    ans.sort()

    if not ans:
        return [-1]
    return [v for k, v in ans]


def main():
    A = [1, 2, 3, 3, 3, 3, 4, 4]
    ret = solution(A)
    ans = [4, 2]
    x = ret == ans
    print(x)
    assert x

    A = [3, 2, 4, 4, 2, 5, 2, 5, 5]
    ret = solution(A)
    ans = [3, 2, 3]
    x = ret == ans
    print(x)
    assert x

    A = [3, 5, 7, 9, 1]
    ret = solution(A)
    ans = [-1]
    x = ret == ans
    print(x)
    assert x


main()
