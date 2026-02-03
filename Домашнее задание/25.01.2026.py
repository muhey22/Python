'''
#Task-1

num = int(input("Введіть число: "))

print("Оберіть степінь:")
print("0 — нульовий")
print("1 — перший")
print("2 — другий")
print("3 — третій")
print("4 — четвертий")
print("5 — п’ятий")
print("6 — шостий")
print("7 — сьомий")

choice = int(input("Ваш вибір: "))

match choice:
    case 0:
        print(num ** 0)
    case 1:
        print(num ** 1)
    case 2:
        print(num ** 2)
    case 3:
        print(num ** 3)
    case 4:
        print(num ** 4)
    case 5:
        print(num ** 5)
    case 6:
        print(num ** 6)
    case 7:
        print(num ** 7)
    case _:
        print("Помилка! Оберіть степінь від 0 до 7.")
'''

'''
#task-2 

num = int(input("Введіть число від 1 до 100: "))

if num < 1 or num > 100:
    print("Помилка! Число має бути в діапазоні від 1 до 100.")
else:
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
'''

'''

#Task-3

total = 0

print("Закуска:")
print("1 — Салат (50 грн)")
print("2 — Суп (40 грн)")
snack = int(input("Ваш вибір: "))

if snack == 1:
    total += 50
elif snack == 2:
    total += 40

print("Основна страва:")
print("1 — Курка (120 грн)")
print("2 — Риба (150 грн)")
main = int(input("Ваш вибір: "))

if main == 1:
    total += 120
elif main == 2:
    total += 150

print("Десерт:")
print("1 — Торт (60 грн)")
print("2 — Морозиво (50 грн)")
dessert = int(input("Ваш вибір: "))

if dessert == 1:
    total += 60
elif dessert == 2:
    total += 50

print("Статус клієнта:")
print("1 — Звичайний")
print("2 — Постійний")
status = int(input("Ваш вибір: "))

if status == 2:
    total = total - total * 0.1

if snack and main and dessert:
    total = total - total * 0.05

print("Вартість обіду:", total, "грн")
'''

