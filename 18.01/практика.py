'''
#Task-1

score = int(input("Введи балл:"))

match score:
    case x if 90 < x < 100:
        print("Відмінно")
    case x if 75 < x < 89:
        print("Добре")
    case x if 69 > x >50:
        print("Задовільно")
    case x if 50 > x :
        print("Незадовільно")
'''

'''
# Task-2

salary = float(input("Введите вашу зарплату: "))
experience = float(input("Введите стаж работы в годах: "))

match experience:
    case x if x < 1:
        print("Премия не предусмотрена")
    case x if 1 <= x < 3:
        print(f"Ваша премия: {salary * 0.05:.2f}")
    case x if 3 <= x <= 5:
        print(f"Ваша премия: {salary * 0.10:.2f}")
    case x if x > 5:
        print(f"Ваша премия: {salary * 0.15:.2f}")
'''

'''
#Task-3 

num = int(input("Введіть чотиризначне число: "))
total = num // 1000 + (num // 100 % 10) + (num // 10 % 10) + (num % 10)

match total % 2:
    case 0:
        print("Сума цифр парна")
    case 1:
        print("Сума цифр непарна")
'''