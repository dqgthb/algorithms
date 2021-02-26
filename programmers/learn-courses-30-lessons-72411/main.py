
import itertools

def solution(orders, course):
    answer = []
    menus = set(menu for order in orders for menu in order)
    orderSet = [set(order) for order in orders]
    for num in course:
        maxCount = 2
        maxCandidates = []
        for course in itertools.combinations(menus, r=num):
            count = 0
            for order in orderSet:
                for menu in course:
                    if menu not in order:
                        break
                else:
                    count += 1
            if count == maxCount:
                maxCandidates.append(course)
            elif count > maxCount:
                maxCandidates = [course]
                maxCount = count
        for candidate in maxCandidates:
            candidate = [i for i in candidate]
            candidate.sort()
            answer.append(''.join(candidate))
    answer.sort()
    return answer


def main():
    ans = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
    print(ans)

if __name__ == "__main__":
    main()