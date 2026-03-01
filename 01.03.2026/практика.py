'''
#task-1

def print_contact(contact):
    if contact['мобільний'] != None: print(f"мобільний: {contact['мобільний']}")
    if contact['робочий'] != None: print(f"робочий: {contact['робочий']}")


def print_formatted_text():
    print('==============================')
    print('        МОЇ КОНТАКТИ')
    print('==============================')
    print('Автор: Олександр')
    print('Версія програми: 1.0')
    print('==============================')


contacts = {
    'Марина' : {
        'мобільний': '0671234567',
        'робочий' : '0449876543'
    },
    'Сергій Майстер' : {
        'мобільний': None,
        'робочий' : '0501112233'
    },
    'Ігор Спортзал' : {
        'мобільний': '0937654321',
        'робочий' : None
    }
}


print_formatted_text()


while True:
    print('1. Знайти контакт\n2. Вивести всі контакти\n0. Вихід')
    action = int(input('Оберіть дію: '))

    match action:
        case 1:
            name = input('Введіть ім\'я контакту:')
            if name in contacts:
                print_contact(contacts[name])
            else:
                print('Немає такого контакту!')
        case 2:
            for contact in contacts:
                print('------------------')
                print(contact)
                print_contact(contacts[contact])
        case 0:
            break
        case _:
            print("Нема такого варіанту!")
            '''

'''
#task-2

def print_odd_numbers(a, b):
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i)


print_odd_numbers(3, 15)
'''


'''
#task-3

def print_line(length, direction, symbol):
    if direction == 'h':
        print(symbol * length)
    else:
        for i in range(length):
            print(symbol)


print_line(7, 'h', '-')
print()
print_line(4, 'v', '*')
'''


'''
#task-4

def max_of_four(a, b, c, d):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    if d > max_num:
        max_num = d
    return max_num


result = max_of_four(12, 45, 7, 33)
print('Максимальне число:', result)
'''


#task-5
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True 