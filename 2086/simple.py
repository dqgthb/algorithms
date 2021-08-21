MOD = 10**9
def main():
    a, b = map(int, input().split())
    ans = (fib(b+2)[0][1] - fib(a+1)[0][1] + MOD) % MOD
    print(ans)


def fib(n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return [[1, 1], [1, 0]]
    elif n % 2 == 0:
        mat = fib(n//2)
        return matMul(mat, mat)
    else:
        mat = fib(n//2)
        return matMul(matMul(mat, mat), [[1, 1], [1, 0]])


def matMul(a, b):
    h1, w1 = len(a), len(a[0])
    h2, w2 = len(b), len(b[0])

    mat = [[0 for _ in range(w2)] for _ in range(h1)]

    for i in range(h1):
        for j in range(w2):
            for k in range(w1):
                mat[i][j] += a[i][k] * b[k][j] % MOD
                mat[i][j] = mat[i][j] % MOD
    return mat

main()