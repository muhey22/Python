'''
# Task-1

numbers = []

count = int(input("Сколько чисел вы хотите ввести: "))

for i in range(count):
    num = int(input("Введите число: "))
    numbers.append(num)

print("Список чисел:", numbers)

total_sum = sum(numbers)
print("Сумма элементов:", total_sum)

if len(numbers) > 0:
    average = total_sum / len(numbers)
    print("Среднее арифметическое:", average)
else:
    print("Список пустой")
'''

'''
# Task-2

numbers = []

print("Введите целые числа. Для завершения введите 0")

num = int(input("Введите число: "))

while num != 0:
    numbers.append(num)
    num = int(input("Введите число: "))

print("Список чисел:", numbers)

search_number = int(input("Введите число, которое нужно найти: "))

number_count = numbers.count(search_number)
print(number_count)


if search_number in numbers:
    print("Число есть в списке")
else:
    print("Числа нет в списке")


while search_number in numbers:
    numbers.remove(search_number)

print("Список после удаления найденных чисел:", numbers)
'''

'''
# Task-3

numbers = []

print("Введите целые числа. Для завершения ввода введите 0")

num = int(input("Введите число: "))

while num != 0:
    numbers.append(num)
    num = int(input("Введите число: "))

print("Список чисел:", numbers)

# находим сумму всех положительных чисел
positive_sum = 0
for n in numbers:
    if n > 0:
        positive_sum += n

print("Сумма всех положительных чисел:", positive_sum)
'''

'''
# Task-4

numbers = []

print("Введите целые числа. Для завершения ввода введите 0")

num = int(input("Введите число: "))

while num != 0:
    numbers.append(num)
    num = int(input("Введите число: "))

print("Список чисел:", numbers)

# находим индексы всех четных чисел
even_indexes = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_indexes.append(i)

print("Индексы всех четных чисел:", even_indexes)
'''
