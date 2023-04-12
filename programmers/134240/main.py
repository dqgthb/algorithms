def solution(food):

    foodArr = []

    for i in range(1, len(food)):
        foodArr.append(str(i) * (food[i] // 2))

    foodStr = "".join(foodArr)
    answer = foodStr + "0" + foodStr[::-1]
    return answer


def main():
    food = [1, 3, 4, 6]
    ans = solution(food)
    result = "1223330333221"
    print(ans)
    assert ans == result

    food = [1, 7, 1, 2]
    ans = solution(food)
    result = "111303111"
    print(ans)
    assert ans == result


main()
