def solution(stones, k):
    count = 0

    return binRight(k, min(stones), max(stones)-1, stones) - 1


def binRight(val, left, right, stones):
    if left == right:
        return left
        
    mid = (left + right) // 2
    midVal = lowerboundK(stones, mid)
        
    if val < midVal:
        return binRight(val, left, mid, stones)
    else:
        return binRight(val, mid+1, right, stones)


def lowerboundK(stones, people):
    people -= 1
    stones = [stone - people for stone in stones]
    maxCount = 0
    count = 0
    for stone in stones:
        if stone <= 0:
            count += 1
            maxCount = max(maxCount, count)
        else:
            count = 0
    return maxCount+1


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
ans = solution(stones, k)
print(ans-1)