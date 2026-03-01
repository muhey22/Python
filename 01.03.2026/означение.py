def print_contact(contact):
    if contact['мобільний'] != None: print(f"мобільний: {contact['мобільний']}")
    if contact['робочий'] != None: print(f"робочий: {contact['робочий']}")

contacts = {
    'Настя' : {
        'мобільний': '0506985764',
        'робочий' : '0890989584'
    },
    'Антон СТО' : {
        'мобільний': None,
        'робочий' : '0500598473'
    },
    'Тимофій Карпати' : {
        'мобільний': '0506985764',
        'робочий' : None
    }
}

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
                print(contact)
                print_contact(contacts[contact])
        case 0: break
        case _: print("Нема такого варіанту!")

        def print_greeting():
    print('==================')
    print('== Hello, USER! ==')
    print('==================')


# print_greeting()

def print_named_greeting(name: str):
    print('==================')
    print(f'== Hello, {name.upper()}! ==')
    print('==================')


print_named_greeting('Vova')
print_named_greeting('Антон')

# print_named_greeting(10)

def print_full_name(last_name, first_name):
    print("Повне ім'я:", last_name, first_name)


print_full_name('Ковальчук', 'Антон')
print_full_name(last_name='Ковальчук', first_name='Антон')


def my_sum(num1: float | int, num2: float | int) -> float | None:
    if type(num1) != float or type(num2) != float:
        return
    return num1 + num2

result = my_sum(10.0, 12.0)
print(result)

def print_full_name(last_name, first_name):
    print("Повне ім'я:", last_name, first_name)


print_full_name('Ковальчук', 'Антон')
print_full_name(last_name='Ковальчук', first_name='Антон')

def my_animal(type, name, age):
    print(f'У мене є {type} на ім\'я {name}. Вік: {age}')


my_animal('собака', age=10, name='Патрон')

def my_sum(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result


print(my_sum(10,12, 34))
print(my_sum(10))
print(my_sum(10,10,10,10,10,10,10,10,10,10,10))

def unpack_positional(a, b, c):
    print(a, b, c, sep=', ')


fruits = ['apple', 'orange', 'banana']
unpack_positional(*fruits)


def unpack_kw_args(red, green, yellow):
    print(red, green, yellow)


fruits = {
    'red': 'apple',
    'green': 'pear',
    'yellow': 'banana'
}

unpack_kw_args(**fruits)


global_var = 12

def local_func(local_param):
    global global_var
    global_var = 50
    local_var = 10 # локальна область видимості
    print(local_var)
    print(global_var)

local_func(10)
print(global_var)


def do_smth():
    print('Щось робимо...')


def main():
    print('Початок роботи!')
    do_smth()
    print('Кінець роботи!')


if __name__ == '__main__':
    main()