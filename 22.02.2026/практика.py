'''
#Task-1

contacts = {}

print("Додаємо контакти")

name1 = input("Введи ім'я: ")
phone1 = input("Введи номер: ")
contacts[name1] = phone1

name2 = input("Введи ім'я: ")
phone2 = input("Введи номер: ")
contacts[name2] = phone2

print("Всі контакти:")
for i in contacts:
    print(i, ":", contacts[i])

print("Зміна контакту")
change_name = input("Кого змінити?: ")

if change_name in contacts:
    new_phone = input("Новий номер: ")
    contacts[change_name] = new_phone
    print("Змінено")
else:
    print("Такого нема")

print("Видалення контакту")
delete_name = input("Кого видалити?: ")

if delete_name in contacts:
    contacts.pop(delete_name)
    print("Видалено")
else:
    print("Такого нема")

print("Кінцевий список контактів:")
for i in contacts:
    print(i, ":", contacts[i])
'''


'''
#Task-2

text = input("Введи текст: ")

text = text.lower()
words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Результат:")

for i in word_count:
    print(i, ":", word_count[i])
'''

'''
#Task-3

rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}

currency = input("Введи валюту (USD, EUR, PLN): ")
amount = float(input("Введи суму в гривнях: "))

if currency in rates:
    result = amount / rates[currency]
    print("Еквівалент у", currency, ":", result)
else:
    print("Такої валюти немає")
'''
