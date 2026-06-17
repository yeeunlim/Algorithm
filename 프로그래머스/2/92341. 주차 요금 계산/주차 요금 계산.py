import math
from collections import defaultdict

def solution(fees, records):
    basic_time, basic_fee, time_unit, fee_per_time = fees
    
    def to_minutes(time):
        h, m = map(int, time.split(':'))
        minutes = h * 60 + m
        return minutes
    # {차량번호: [입차/출차 시간] 스택}
    car_records = defaultdict(list)
    # {차량번호: 누적 주차 시간}
    car_park_time = defaultdict(int)
    for record in records:
        time, car_num, inout = record.split()
        time_int = to_minutes(time)
        if inout == 'IN':
            car_records[car_num].append(time_int)
        else:
            in_time = car_records[car_num].pop()
            park_time = time_int - in_time
            car_park_time[car_num] += park_time
    print(car_records)
    for car_num in car_records:
        if car_records[car_num]:
            park_time = to_minutes('23:59') - car_records[car_num][0]
            car_park_time[car_num] += park_time
    car_park_time = dict(sorted(car_park_time.items()))
    
    car_fees = [basic_fee + math.ceil(max(car_park_time[key] - basic_time, 0) / time_unit) * fee_per_time for key in car_park_time]
    
    return car_fees
            