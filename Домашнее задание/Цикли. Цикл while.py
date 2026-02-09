'''
#Task-1

num_1 = int(input())
num_2 = int(input())

i = num_1
while i <= num_2:
    if i % 7 == 0:
        print(i)
    i = i + 1
'''

'''
#Task-2 

num_1 = int(input())
num_2 = int(input())

i = num_1
while i <= num_2:
    print(i)
    i = i + 1

i = num_2
while i >= num_1:
    print(i)
    i = i - 1

i = num_1
while i <= num_2:
    if i % 7 == 0:
        print(i)
    i = i + 1

count = 0
i = num_1
while i <= num_2:
    if i % 5 == 0:
        count = count + 1
    i = i + 1

print(count)
'''

'''
#Task-3

num_1 = int(input())
num_2 = int(input())

num = num_1
while num <= num_2:
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    num = num + 1
'''


#Task-4

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))
step = int(input("Введіть крок: "))
order = input("Прямий порядок чи зворотний? (прямий/зворотний): ")

if order == "прямий":
    num = start
    while num <= end:
        print(num)
        num = num + step
elif order == "зворотний":
    num = end
    while num >= start:
        print(num)
        num = num - step
else:
    print("Невірний вибір порядку")

