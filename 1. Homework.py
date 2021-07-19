# My homework №1. Yuri Shemetov

words = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"

# Шаг 1 - Количество символов 
quantity = len(words)
print("Шаг 1 - Количество символов - " + str(quantity))

# Шаг 2 - Развернутое предложение 
conversely = words[::-1]
print("Шаг 2 - Развернутая строка - " + conversely)

# Шаг 3 - Каждое слово с большой буквы
big_letter = words.title()
print("Шаг 3 - Каждое слово с большой буквы - " + big_letter)

# Шаг 4 - Весь текст прописными буквами
big_letters = words.upper()
print("Шаг 4 - Весь текст прописными буквами - " + big_letters)

# Шаг 5 - Число вхождениий "нд", "ам", "о" в строке (без использования метода count)
nd = 0
index_d = 0
am = 0
index_m = 0
o = 0
for i in words[:-1]:
    index_d += 1 
    if  i == 'н' and words[index_d] == 'д':
        nd += 1
for k in words[:-1]:
    index_m += 1 
    if  k == 'а' and words[index_m] == 'м':
        am += 1  
for j in words:
    if j == 'о':
        o += 1 
print("Шаг 5 - Количество встречающихся 'нд': ", str(nd),
    "\n\tКоличество встречающихся 'ам': " + str(am),
    "\n\tКоличество встречающихся 'o': " + str(o))

# Шаг 6 Собственные упражнения
little_letter = words.lower()
print("Шаг 6 - Каждое слово с маленькой буквы - " + little_letter)
print("\t Разбиение предложения на список слов - ",  words.split())
print("\t Вставка символа '.' между буквами и прочими символами - ",  '.'.join(words))
print("\t Cклейка текса на позиции [50:72] и [-1:] - ",  words[50:72], words[-1:])

# Шаг 7 Исходная строка
print("Шаг 7 - Исходная строка - ", words)