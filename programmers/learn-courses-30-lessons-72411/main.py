
import itertools

def solution(orders, course):
    menus = set(menu for order in orders for menu in order)
    print(menus)

    for menu in course:



def courseMenu(numOfCourse):






def main():
    ans = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
    ans = solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
    print(ans)

if __name__ == "__main__":
    main()