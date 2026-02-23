'''
# Task-2

import random

first = set()
second = set()

for i in range(10):
    first.add(random.randint(1, 20))
    second.add(random.randint(1, 20))

print("Перша множина:", first)
print("Друга множина:", second)

intersection = first & second
difference = first - second
union = first | second

print("Спільні елементи:", intersection)
print("Різниця:", difference)
print("Об'єднання:", union)
'''


# Task-3

word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

set1 = set(word1.lower())
set2 = set(word2.lower())

if set1 == set2:
    print("Слова є анаграмами")
else:
    print("Слова не є анаграмами")