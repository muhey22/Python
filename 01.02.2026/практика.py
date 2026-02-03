'''
#Task-1

number = int(input('Введіть число: '))

for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')
'''

'''
#Task-2 
for i in range(1, 10):
    print('Таблиця множення для', i)
    for j in range(1, 10):
        print(i, 'x', j, '=', i * j)
    print()
'''

'''
#Task-3

num = int(input('Скільки чисел будете вводити? '))

max_number = None

for i in range(num):
    number = int(input('Введіть число: '))
    
    if max_number is None or number > max_number:
        max_number = number

print('Найбільше число:', max_number)
'''


#Task-4


