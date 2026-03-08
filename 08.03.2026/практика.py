'''
#Task-1

def get_power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * get_power(base, exponent - 1)

numbers = [2, 3, 5]
exponents = [3, 2, 4]
powered_numbers = []

for i in range(len(numbers)):
    powered_numbers.append(get_power(numbers[i], exponents[i]))

print(powered_numbers)
'''


'''
#Task-2 

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def date_difference(d1, m1, y1, d2, m2, y2):
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    def days_from_start(day, month, year):
        days = sum(days_in_month[:month-1]) + day
        if month > 2 and is_leap_year(year):
            days += 1
        return days

    if y1 == y2:
        return abs(days_from_start(d1, m1, y1) - days_from_start(d2, m2, y2))

    days_first_year = (366 if is_leap_year(y1) else 365) - days_from_start(d1, m1, y1)
    days_last_year = days_from_start(d2, m2, y2)
    days_middle_years = 0
    for y in range(y1 + 1, y2):
        days_middle_years += 366 if is_leap_year(y) else 365

    return days_first_year + days_middle_years + days_last_year

d1, m1, y1 = 15, 3, 2023
d2, m2, y2 = 10, 3, 2026

result = date_difference(d1, m1, y1, d2, m2, y2)
print(result)
'''


#Task-3

numbers = [random.randint(1, 100) for _ in range(100)]

def min_sum_position(lst, start=0, min_pos=0, min_sum=None):
    if start > len(lst) - 10:
        return min_pos
    current_sum = sum(lst[start:start+10])
    if min_sum is None or current_sum < min_sum:
        min_sum = current_sum
        min_pos = start
    return min_sum_position(lst, start + 1, min_pos, min_sum)

position = min_sum_position(numbers)
print(position)
