from datetime import datetime
import math
from collections import defaultdict
def solution(fees, records):
    defaultTime, defaultCost, unitTime, unitCost = fees

    answer = []
    cars = {}
    totalHours = defaultdict(int)
    for record in records:
        time, num, inOut = record.split()
        if inOut == "IN":
            cars[num] = datetime.strptime(time, '%H:%M')
        else:
            delta = datetime.strptime(time, '%H:%M') - cars[num]
            totalHours[num] += delta.seconds // 60
            del cars[num]

    lastMinute = datetime.strptime("23:59", '%H:%M')
    for carsLeft in cars:
        totalHours[carsLeft] += (lastMinute - cars[carsLeft]).seconds // 60

    fees = defaultdict(lambda:defaultCost)
    for car in totalHours:
        totalH = totalHours[car]
        if totalHours[car] >= defaultTime:
            fees[car] += math.ceil((totalHours[car] - defaultTime) / unitTime) * unitCost
        else:
            fees[car]
    lst = [i for i in fees.items()]
    lst.sort()
    return [j for i, j in lst]




def main():
    pass
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    print(solution(fees, records))

if __name__ == "__main__":
    main()