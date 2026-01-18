'''
#Task-1

number = int(input("Введите число"))

if number %2 == 0:
    print("Even number", number)

else:
    print("Odd number", number)


#Task-2

number = int(input("Введите число"))

if number % 7 == 0:
    print("Number is multiple 7", number)

else:
    print("Number is not multiple 7", number)


#Task-3

number_1 = float(input("Введите первое число"))

number_2 = float(input("Введите второе число"))

if number_1 > number_2:
    print("большее число", number_1)
elif number_1 < number_2: 
    print("большее число", number_2)
elif number_1 == number_2:
    print("оба числа равны")


#Task-4

number_1 = float(input("Введите первое число"))

number_2 = float(input("Введите второе число"))

if number_1 > number_2:
    print("Меньшее число", number_2)
elif number_2 > number_1:
    print("Меньшее число", number_1)
else:
    print("оба числа равны")
'''

#Task-5

number_1 = float(input("Введите первое число"))

number_2 = float(input("Введите второе число"))

operation = input("выберете действие(сумма, умножение, разницу)")

if operation =="сумма":
    print(f'{number_1} + {number_2} {number_1 + number_2}')
elif operation == "умножение":
    print(f'{number_1} * {number_2} {number_1 * number_2}')
elif operation == "разница":
    print(f'{number_1} - {number_2} {number_1 - number_2}')
else:
    print("Выбраное неправильное действие")
