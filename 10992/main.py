
n = int(input())

if n > 1:
    print(" " * (n - 1) + "*")

for i in range(1, n-1):
    firstBlank = n - i - 1
    secondBlank = i * 2 - 1
    print(" " * firstBlank + "*" + secondBlank * " " + "*")



print((2*n - 1) * '*')