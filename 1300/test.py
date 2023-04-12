from math import floor, log2, sqrt

global N
N = 3


arr = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        arr.append(i * j)

arr.sort()
print(arr)

mat = [[i * j for j in range(1, N+1)] for i in range(1, N+1)]
print(*mat, sep="\n")


def numbersLowerOrEqualTo(num):
    p = floor(sqrt(num))

    cnt = p * p

    # i * q + r = num
    for i in range(p + 1, N + 1):
        q, r = divmod(num, i)

        if q == 0:
            break

        cnt += 2 * q
    return cnt


for i in range(1, N ** 2 + 1):
    print(i, numbersLowerOrEqualTo(i))


# 100 101 102 ... 140
# 10  10  10 ...  11
