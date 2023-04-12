

def solution(k, m, score):
    score.sort(reverse=True)
    total = 0
    for i in range(m - 1, len(score), m):
        small = score[i]
        total += m * small
    return total


def main():
    k, m, score = 3, 4, [1, 2, 3, 1, 2, 3, 1]
    ans = solution(k, m, score)
    print(ans)
    assert ans == 8

    k, m, score = 4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
    ans = solution(k, m, score)
    print(ans)
    assert ans == 33


if __name__ == "__main__":
    main()
