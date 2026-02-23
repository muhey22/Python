'''
#Task-1 

num = float(input("Введіть число: "))
power = int(input("Введіть степінь (від 0 до 7): "))

match power:
    case 0:
        print("Результат:", num ** 0)
    case 1:
        print("Результат:", num ** 1)
    case 2:
        print("Результат:", num ** 2)
    case 3:
        print("Результат:", num ** 3)
    case 4:
        print("Результат:", num ** 4)
    case 5:
        print("Результат:", num ** 5)
    case 6:
        print("Результат:", num ** 6)
    case 7:
        print("Результат:", num ** 7)
    case _:
        print("Помилка! Степінь повинен бути від 0 до 7.")
        '''


#Task-2

num = int(input("Введіть число (від 1 до 100): "))

if 1 <= num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
else:
    print(num)
    