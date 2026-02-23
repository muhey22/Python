'''
# Task-1

dictionary = {
    "apple": "яблуко",
    "car": "машина",
    "house": "будинок",
    "dog": "собака",
    "cat": "кіт"
}

word = input("Введіть слово англійською: ").lower()

if word in dictionary:
    print("Переклад:", dictionary[word])
else:
    print("Слово не знайдено")
    '''

# Task-2

n = int(input("Скільки у вас друзів? "))

my_games = set(input("Введіть ваші ігри через пробіл: ").split())

common_games = my_games

for i in range(n):
    friend_games = set(input("Введіть ігри друга через пробіл: ").split())
    common_games = common_games & friend_games

print("Ігри, в які можуть зіграти всі разом:", common_games)