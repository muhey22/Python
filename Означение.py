'''print("Hello, world")
print(10)
print(10, 12, 14)
print(10, 5, 6, 6 ,sep=', ')

# Тип даних - характеристика даних, яка визначає діапазон значень та набір доступних операцій.

# str - послідовність символів
# int - цілі числа
# float - дробові числа

print(type(10 / 5))

# Змінна - іменована область пам'яті, що зберігає значення певного типу і може його змінювати
# протягом виконання програми.

group = 'П511'
print(type(group))
group = 511
print(type(group))

weather = input('Введіть поточну погоду: ')
print(weather)











number1 = float(input("Введіть число: "))
print(type(number1))
number2 = float(input("Введіть число: "))
print(f'{number1} ** {number2} = {number1 ** number2}')











number1 = float(input("Введіть число: "))
print(type(number1))
number2 = float(input("Введіть число: "))
print(f'{number1} ** {number2} = {number1 ** number2}')












number = int(input("Введіть ціле число: "))

print(f'{number} > 10? {number > 10}')
print(f'{number} >= 10? {number >= 10}')
print(f'{number} < 10? {number < 10}')
print(f'{number} <= 10? {number <= 10}')
print(f'{number} == 10? {number == 10}')
print(f'{number} != 10? {number != 10}')











is_raining = input("Чи іде зараз дощ? (так/ні) ")

if is_raining == 'так':
    print("Беремо парасолю!")

is_cold = input("Чи зараз холодно? (так/ні)")

if is_cold == 'так':
    print('Вдягаємо теплий одяг')
else:
    print('Вдягаємо легкий одяг')

print('Виходимо на вулицю!')











is_raining = input("Чи іде зараз дощ? (так/ні) ")

if is_raining == 'так':
    print("Беремо парасолю!")

'''
# is_cold = input("Чи зараз холодно? (так/ні)")

# if is_cold == 'так':
#     print('Вдягаємо теплий одяг')
# else:
#     print('Вдягаємо легкий одяг')
'''

temperature = int(input("Скільки зараз градусів на вулиці? "))

if temperature <= -10:
    print('Вдягаємось дуже тепло: рукавички, термобілизна, зимова шуба, зимові штанці, черевики')
elif temperature > -10 and temperature <= 5: # else if
    print('Вдягаємо тепло: куртка, теплі штанці, теплі кросівки')
elif temperature > 5 and temperature <= 16:
    print('Вдягаємось легко: кофта, сорочка, кеди, легкі штанці')
else:
    print("Вдягаємось по-літньому: футболка, шорти, шкльопки і на море!")

print('Виходимо на вулицю!')











boolean = bool(0) # False

print(bool(0)) # False
print(bool(0.0)) # False
print(bool('')) # False

something = None
print(bool(something)) #

print(bool(10)) # True
print(bool(-6.8)) # True
print(bool('hello')) # True
 












# Калькулятор. Користувач вводить два числа та обирає операцію (+ - * /). Програма виводить результат.
number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))

operation = input('Оберіть операцію (+, -, *, /): ')

if operation == '+':
    print(f'{number1} + {number2} = {number1 + number2}')
elif operation == '-':
    print(f'{number1} - {number2} = {number1 - number2}')
elif operation == '*':
    print(f'{number1} * {number2} = {number1 * number2}')
elif operation == '/':
    if number2 == 0:
        print('Не можна ділити на нуль!')
    else:
        print(f'{number1} / {number2} = {number1 / number2}')
else:
    print('Некоректна операція!')
    '''

















'''

a = 100
b = 50

print("a > b") if a > b else("a < b")

'''













'''
login = input('Введите ваш логин')

display_name = login if login else'гость'

print(f'Привет, {display_name}')
'''









'''
age = 18

if age <18:
    pass 
else:
    print("Full access granted")
'''
'''
day = int(input("Введите день"))

if day == "1":
    print("Понидельник")

if day == "2":
    print("Вторник")

if day == 3":
    print("Среда")
'''

'''
day = int(input("Введите день"))

match day:
    case 1: print('Понидельник')
    case 2: print('Вторник')
    case 2: print('Среда')
    case _: print('не коренктный норме дня')
'''

'''
month = int(input("Введите месяц"))

match month:
    case 12 | 1 | 2: print('Зима')
    case 3 | 4 | 5: print('Весна')
    case 6 | 7 | 8: print('Лето')
    case 9 | 10 | 11: print('Осень')
'''
'''
month = int(input("Введите месяц"))
day = int(input("Введите день"))

match day:
    case 1| 2 | 3 | 4 | 5 if month == 12:
        print('Будний день в декобре')
    case 1 | 2 | 3 | 4 | 5 if month == 1:
        print('Будний день в январе')
    case 6 | 7 if month == 12:
        print('выходной день в декобре')
    case 6 | 7 if month == 1:
        print('выходной день в январе')
    
    
'''

