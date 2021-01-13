N = int(input())

def sumOfDigits(n):
    return sum([int(i) for i in list(str(n))])

for i in range(N):
    if N == i + sumOfDigits(i):
        print(i)
        break
else:
    print(0)


