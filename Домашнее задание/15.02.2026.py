'''
# Task-1

numbers = []

count = int(input("Сколько чисел вы хотите ввести: "))

for i in range(count):
    num = int(input("Введите число: "))
    numbers.append(num)

print("Список чисел:", numbers)

N = int(input("Введите количество позиций для сдвига вправо: "))

if len(numbers) > 0:

    N = N % len(numbers)

    for i in range(N):
        last = numbers[-1]
        
        for j in range(len(numbers) - 1, 0, -1):
            numbers[j] = numbers[j - 1]
        
        numbers[0] = last

    print("Сдвинутый список:", numbers)

else:
    print("Список пустой")
    '''

# Task-2

import random

list1 = []
list2 = []

for i in range(10):
    list1.append(random.randint(1, 20))
    list2.append(random.randint(1, 20))

print("Первый список:", list1)
print("Второй список:", list2)

third1 = list1 + list2
print("Объединение списков:", third1)

third2 = list(set(third1))
print("Без повторений:", third2)

third3 = []
for num in list1:
    if num in list2 and num not in third3:
        third3.append(num)
print("Общие элементы:", third3)

third4 = []
for num in list1:
    if num not in list2:
        third4.append(num)
for num in list2:
    if num not in list1:
        third4.append(num)
print("Только уникальные элементы:", third4)

third5 = [min(list1), max(list1), min(list2), max(list2)]
print("Минимальные и максимальные элементы:", third5)