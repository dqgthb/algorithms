
bonus = 0

for i in range(1300):
    val = round(175 * (1 - 0.995 ** i))
    if bonus != val:
        print(i, val)
        bonus = val

