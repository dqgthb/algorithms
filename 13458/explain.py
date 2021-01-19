arr = [1, 2, 3, 4, 5]


C = []
for i in arr:
    C.append(i*2)
print(C)


def multiplyBy2(x):
    return x*2

A = list(map(multiplyBy2, arr))
print(A)

B = [i*2 for i in arr]
print(B)