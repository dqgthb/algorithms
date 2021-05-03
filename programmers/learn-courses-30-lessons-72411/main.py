import collections
import itertools

def solution(orders, course):
    orders = [list(order) for order in orders]
    for order in orders:
        order.sort()

    orderSet = [set(order) for order in orders]

    courses = []

    for courseNum in course:
        alreadyConsidered = set()
        counter = collections.Counter()
        for orderNum, order in enumerate(orders):
            for courseCandidate in itertools.combinations(order, r = courseNum):
                courseCandidate = tuple(sorted(courseCandidate))
                if courseCandidate in alreadyConsidered:
                    continue
                else:
                    alreadyConsidered.add(courseCandidate)
                    for nextOrderNum in range(orderNum + 1, len(orderSet)):
                        order = orderSet[nextOrderNum]
                        if set(courseCandidate) <= order:
                            counter[courseCandidate] += 1
        if len(counter) > 0:
            maxFreq = max(counter.values())
            for course in counter:
                if counter[course] == maxFreq:
                    courses.append(course)
    courses = [''.join(course) for course in courses]
    courses.sort()
    return courses


def main():
    #ans = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
    ans = solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
    print(ans)

if __name__ == "__main__":
    main()