# Calculator BMI / Developed by Yuri Shemetov
weight = input("Введите  ваш вес (в килограммах): ")
height = input("Введите ваш рост (в сантиметрах): ")
gender = input("Введите ваш пол ('м' или 'ж'): ")
try:
    bmi = round(int(weight)/((int(height)/100)**2))
    print("Ваш индекс массы тела: ", bmi)
    if bmi < 20 and gender == 'м' or bmi < 18 and gender == 'ж':
        print("У вас дефицит массы тела! Обратитесь к врачу!")
    elif bmi > 40 and gender == 'м' or bmi > 30 and gender == 'ж':
        print("У вас избыточный вес! Обратитесь к врачу!")
    elif bmi > 19 and bmi < 41  and gender == 'м':
        scale = "====================="
        scale_lis = list(scale)
        index_indicator = bmi - 20
        scale_lis.pop(int(index_indicator))
        scale_lis.insert(index_indicator, '|')
        print("19" + ''.join(scale_lis) + "41")
    elif bmi > 17 and bmi < 31  and gender == 'ж':
        scale = "============="
        scale_lis = list(scale)
        index_indicator = bmi - 18
        scale_lis.pop(int(index_indicator))
        scale_lis.insert(index_indicator, '|')
        print("17" + ''.join(scale_lis) + "31")
    else:
        print("Чтобы получить более точные данные по шкале, перезапустите программу и введите свой пол! ('м' или 'ж')")
except ValueError:
    print("Данные введены некорректно!\
        \nПерезапустите программу и вводите только целые числа!")