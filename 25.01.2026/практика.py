'''
#task_1
num_1 = int(input("Введіть перше число: "))
num_2 = int(input("Введіть друге число: "))

match num_1 <= num_2:
    case True:
        while num_1 <= num_2:
            print(num_1)
            num_1 += 1
    case False:
        while num_1 >= num_2:
            print(num_1)
            num_1 -= 1

'''

'''
#task_2

num_1 = int(input("Введіть перше число: "))
num_2 = int(input("Введіть друге число: "))

match num_1 <= num_2:
    case True:
        while num_1 <= num_2:
            if num_1 % 2 != 0:   
                print(num_1)
            num_1 += 1
    case False:
        while num_1 >= num_2:
            if num_1 % 2 != 0:  
                print(num_1)
            num_1 -= 1
'''


'''
#task_3

num_1 = int(input("Введіть перше число: "))
num_2 = int(input("Введіть друге число: "))

if num_1 >= num_2:
    current = num_1
    while current >= num_2:
        if current % 2 == 0:
            print(current)
        current -= 1
else:
    current = num_2
    while current >= num_1:
        if current % 2 == 0:
            print(current)
        current -= 1
'''


#task_4

num_1 = int(input("Введіть перше число: "))
num_2 = int(input("Введіть друге число: "))

print("Оберіть порядок відображення чисел:")
print("1 — від меншого до більшого")
print("2 — від більшого до меншого")
choice = int(input("Ваш вибір: "))

match choice:
    case 1:
        current = num_1
        while current <= num_2:
            print(current)
            current += 1
    case 2:
        current = num_1
        while current >= num_2:
            print(current)
            current -= 1
