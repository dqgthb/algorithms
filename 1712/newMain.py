a, b, c = map(int, input().split())

if b >= c:
    print(-1)
    exit(0)

profit = c - b

q, r = divmod(a, profit)

print(q + 1)