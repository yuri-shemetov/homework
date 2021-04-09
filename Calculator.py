# Calculator BMI / Developed by Yuri Shemetov
weight = input("Введите  ваш вес (в килограммах): ")
height = input("Введите ваш рост (в сантиметрах): ")
try:
    bmi = round(int(weight)/((int(height)/100)**2))
    print("Ваш индекс массы тела: ", bmi)

    if bmi < 18:
        print("У вас дефицит массы тела! Обратитесь к врачу!")
    elif bmi > 40:
        print("У вас ожирение! Обратитесь к врачу!")
    else:
        scale = "======================="
        scale_lis = list(scale)
        index_indicator = bmi - 18
        scale_lis.pop(int(index_indicator))
        scale_lis.insert(index_indicator, '|')
        print("17" + ''.join(scale_lis) + "41")
except ValueError:
    print("Данные введены некорректно!\
        \nПерезапустите программу и вводите только целые числа!")