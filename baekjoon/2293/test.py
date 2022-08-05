n, k = map(int, input().split())
k+=1
arr = [int(input()) for _ in range(n)]
arr.sort()

dpArr = [0] * k
result = [0] * k
for i in range(k):
    dpArr[i] = int((i % arr[0]) == 0)

for i in range(1, n):
    for j in range(k):
        newCoin = arr[i]
        result[j] = 0
        for prevK in range(j, -1, -newCoin):
            result[j] += dpArr[prevK]
    for i in range(len(dpArr)):
        dpArr[i] = result[i]
print(dpArr[k-1])
