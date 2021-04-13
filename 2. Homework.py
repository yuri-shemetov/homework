number_1 = int(input("Введите 1-е число: "))
number_2 = int(input("Введите 2-е число: "))
number_3 = int(input("Введите 3-е число: "))
answer_1 = number_1 and number_2 and number_3 and "Нет нулевых значений!"
print("Ответ 1: ", answer_1)
answer_2 = number_1 or number_2 or number_3 or "Введены все нули!"
print("Ответ 2: ", answer_2)
if number_1 >(number_2 + number_3):
    print("Ответ 3: ", number_1, "-", number_2, "-", number_3, "=",\
          (number_1 - number_2 - number_3))
elif number_1 <(number_2 + number_3):
    print("Ответ 3: ", number_2, "+", number_3, "-", number_1, "=", \
          (number_2 + number_3 - number_1))
if number_1 > 50 and (number_2 > number_1 or number_3 > number_1):
    print("Ответ 4: Вася")
if number_1 > 5 or number_2 == number_3 == 7:
    print("Последний ответ: Петя")