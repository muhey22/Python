'''
#Task-1

text = input("Введіть текст: ")

count = 0
for char in text:
    if char == "." or char == "!" or char == "?":
        count += 1

print("Кількість речень у тексті:", count)
'''

'''
# Task-2

text = input("Введіть рядок: ")

clean_text = ""
for char in text:
    if char.isalnum():
        clean_text += char.lower()

reverse_text = ""
for char in clean_text:
    reverse_text = char + reverse_text

if clean_text == reverse_text:
    print("Це паліндром")
else:
    print("Це не паліндром")
      '''

'''

 # Task-3
 
 text = input("Введіть текст: ")

reserved_words = ["python", "if", "else", "for", "while"]

words = text.split()

for i in range(len(words)):
    word_clean = ""
    for char in words[i]:
        if char.isalnum():
            word_clean += char.lower()
    if word_clean in reserved_words:
        words[i] = words[i].upper()

new_text = ""
for word in words:
    new_text += word + " "

print("Змінений текст:", new_text.strip())
  '''

'''
# Task-4

text = input("Введіть рядок: ")
char1 = input("Введіть перший символ: ")
char2 = input("Введіть другий символ: ")

start = -1
end = -1

for i in range(len(text)):
    if text[i] == char1 and start == -1:
        start = i
    if text[i] == char2 and start != -1:
        end = i
        break

if start != -1 and end != -1:
    result = ""
    for i in range(len(text)):
        if i < start or i > end:
            result += text[i]
else:
    result = text

print("Результат:", result)
'''

'''

 # Task-5

 text = input("Введіть текст: ")
chars = input("Введіть символи: ")

words = text.split()
result_words = []

for word in words:
    keep = True
    for c in word:
        if c in chars:
            keep = False
            break
    if keep:
        result_words.append(word)

result = ""
for word in result_words:
    result += word + " "

print("Результат:", result.strip()) 
 '''



# Task-6

text = input("Введіть текст: ")

words = text.split()
reverse_words = []

for i in range(len(words)-1, -1, -1):
    reverse_words.append(words[i])

result = ""
for word in reverse_words:
    result += word + " "

print("Зворотний текст:", result.strip())
