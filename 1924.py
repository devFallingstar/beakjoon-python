# https://www.acmicpc.net/problem/1924

day_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_name = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', ]

date_str = input()
month, day = map(int, date_str.split(' '))

total_passed_days = 0

for each_day in day_per_month[:month]:
    total_passed_days += each_day

total_passed_days += day

print(day_name[(total_passed_days % 7)])