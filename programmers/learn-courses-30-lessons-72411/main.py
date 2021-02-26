
import itertools

def solution(orders, course):
    answer = []
    menus = set(menu for order in orders for menu in order)
    orderSet = [set(order) for order in orders]
    for num in course:
        maxCount = 0
        for course in itertools.product(menus, repeat=num):
            count = 0
            for order in orderSet:
                for menu in course:
                    if menu not in order:
                        break
                else:
                    count += 1
            maxCount = max(count, maxCount)
        answer.append(maxCount)


    return answer


def main():
    solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])

if __name__ == "__main__":
    main()