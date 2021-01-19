arr = [1, 2, 3, 4, 5]


E = [0, 0, 0, 0, 0]
i = 0
while i < len(E):
    print(i, end = ' ')
    E[i] = arr[i] * 2
    i += 1
print(E)
