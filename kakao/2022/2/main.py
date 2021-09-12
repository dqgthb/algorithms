
sieve = None
def solution(n, k):
    global sieve
    if sieve is None:
        sieve = [True for _ in range(1000001)]
        sieve[0] = False
        sieve[1] = False
        N = len(sieve)
        for i in range(2, N):
            for j in range(2, N):
                if i * j < N:
                    sieve[i*j] = False
                else:
                    break

    str_ = convertToK(n, k)
    print(str_)
    lst = [int(i) for i in str_.split("0") if i != '']
    print(lst)
    cnt = 0
    for i in lst:
        if i >= len(sieve):
            if largeNumberPrimeTest(i):
                cnt += 1
            continue
        elif sieve[i]:
            cnt += 1

    return cnt

def convertToK(n, k):
    if n == 0:
        return [0]

    nums = []
    q = n
    while q > 0:
        q, r = divmod(q, k)
        nums.append(r)
    str_ = ''.join(map(str, reversed(nums)))
    return str_

def largeNumberPrimeTest(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def main():

    n = 1000000
    k = 3
    print(solution(n, k))
    return

    n = 437674
    k = 3
    #ans = solution(n, k)
    #print(ans)

    n = 110011
    k = 10
    ans = solution(n, k)
    print(ans)

    n = 91111
    k = 10
    ans = solution(n, k)
    print(ans)


if __name__ == "__main__":
    main()