def solution(stones, k):
    count = 0
    while countConsecutiveZeros(stones) < k:
        min_ = min(i for i in stones if i != 0)
        stones = [i - min_ if i - min_ >= 0 else 0 for i in stones]
        count += min_
    return count

def countConsecutiveZeros(stones):
    count = 0
    maxCount = 0
    for stone in stones:
        if stone == 0:
            count += 1
            maxCount = max(count, maxCount)
        else:
            count = 0
    return maxCount


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
ans = solution(stones, k)
print(ans)