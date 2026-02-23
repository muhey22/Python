'''
first = {'apple', 'mango', 'cherry', 'kiwi'}
second = {'mango', 'pamelo', 'kiwi', 'orange'}

difference = first.difference(second)
difference = first - second
print(difference)

first.difference_update(second)
'''





'''
first = {'apple', 'mango', 'cherry', 'kiwi'}
second = {'mango', 'pamelo', 'kiwi', 'orange'}

intersection = first.intersection(second)
intersection = first & second # оператор &

print(intersection)

# union = first.union(second)
# union = first | second # оператор or
# print(union)
print(first)
print(second)
'''






'''my_set = set()
my_set = set( ['apple', 'cherry', 'mango'] )

my_set = { 'apple', 'cherry', 'mango', 'mango' }

print(my_set)
print(type(my_set))

# print(my_set[0])
# my_set[1] = 'pamelo'

print(len(my_set))

new_set = {True, 1, 0, False}
print(len(new_set))
print(new_set)

for item in my_set:
    print(item)

print('apple' in my_set)
print('banana' not in my_set)'''







'''
first = {'apple', 'mango', 'cherry', 'kiwi'}
second = {'mango', 'pamelo', 'kiwi', 'orange'}

intersection = first.intersection(second)
intersection = first & second # оператор &

first.intersection_update(second)

print(intersection)
'''



'''
first = {'apple', 'mango', 'cherry', 'kiwi'}
second = {'mango', 'pamelo', 'kiwi', 'orange'}

difference = first.difference(second)
difference = first - second
print(difference)

first.difference_update(second)
'''


'''
sym_diff = first.symmetric_difference(second)
sym_diff = first ^ second # оператор XOR
print(sym_diff)

first.symmetric_difference_update(second)
'''



'''
first = {'apple', 'mango', 'cherry', 'kiwi'}
second = {'mango', 'pamelo', 'kiwi', 'orange'}

frozen_food = frozenset(first | second)

print(frozen_food)
print(type(frozen_food))

# frozen_food.add('watermelon') Помилка!
# '''


'''
contacts = {
    'Антон': '0506959068',
    'Ліза': '0474838458',
    'Сергій': '0550404033'
}

print(contacts['Ліза'])
contacts['Сергій'] = '0650499596'
print(contacts['Сергій'])

contacts['Настя'] = '0500440405'
print(contacts['Настя'])

contacts.update({'Антон': '0670450044', 'Тимофій': '0897477744'})

print(contacts)

'''



'''
print(contacts.keys())
print(contacts.values())
print(contacts.items())

for i in contacts:
    print(f"{i}: {contacts[i]}")
'''

'''
contacts.pop('Настя')
contacts.popitem()
contacts.clear()
 
'''



'''
employees = {
    '1': {
        'name' : 'Антон',
        'position': 'Junior .NET Developer',
        'salary': 20000
    },
    '2': {
        'name' : 'Анастасія',
        'position':'Team Lead',
        'salary': 115000
    },
    '3': {
        'name' : 'Кирило',
        'position': 'Senior .NET Developer',
        'salary': 90000
    }
}

print(employees['2']['position'])
'''


