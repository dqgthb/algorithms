arr = [1, 2, 3, 4, 5]


E = [0, 0, 0, 0, 0]
i = 0
while i < len(E):
    print(i, end = ' ')
    E[i] = arr[i] * 2
    i += 1
print(E)


D = [0, 0, 0, 0, 0]
for i in range(len(D)):
    print(i, end = ' ')
    D[i] = arr[i] * 2
print(D)


C = []
for i in arr:
    C.append(i*2)
print(C)


A = list(map(lambda x: x*2, arr))
print(A)


B = [i*2 for i in arr]
print(B)