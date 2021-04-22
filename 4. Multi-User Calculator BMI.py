def show_menu()-> int:
    MENU = """
    1. List
    2. Create
    3. Read
    4. Update
    5. Delete
    6. Quit
    """
    print(MENU)
    return int(input("Your answer: "))

USERS = {}

def list_users():
    for key, value in USERS.items():
        print(key, ': ', value)

def create_user():
    login = input("Введите ваше имя: ")
    height = input("Введите ваш рост (cm): ")
    weight = input("Введите ваш вес (kg): ")
    gender = input("Введите ваш пол(m/w): ")

    USERS[login] = [height, weight, gender]
    
def read_user():
    user = input("Введите имя зарегистрированного пользователя: ")
    for key, value in USERS.items():
        if key == user:
            height = value[0]
            weight = value[1]
            gender = value[2]
    # Ниже используется ранее написанный код калькулятора !!!
    try:
        bmi = round(int(weight)/((int(height)/100)**2))
        print("Ваш индекс массы тела: ", bmi)
        if bmi < 20 and gender == 'm' or bmi < 18 and gender == 'w':
            print("У вас дефицит массы тела! Обратитесь к врачу!")
        elif bmi > 40 and gender == 'm' or bmi > 30 and gender == 'w':
            print("У вас избыточный вес! Обратитесь к врачу!")
        elif bmi > 19 and bmi < 41  and gender == 'm':
            scale = "====================="
            scale_lis = list(scale)
            index_indicator = bmi - 20
            scale_lis.pop(int(index_indicator))
            scale_lis.insert(index_indicator, '|')
            print("19" + ''.join(scale_lis) + "41")
        elif bmi > 17 and bmi < 31  and gender == 'w':
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

def update_user():
    user = input("Введите имя зарегистрированного пользователя: ")
    for key, value in USERS.items():
        if key == user:
            value[0] = int(input("Ваш новый рост (cm): "))
            value[1] = int(input("Ваш новый вес (kg): "))
            print("Ваши данные успешно изменены!")
    if user not in USERS.keys():
        print("Пользователя с таким именем не существует!")

def delete_user():
    user = input("Введите имя зарегистрированного пользователя: ")
    try:  
        del USERS[user]
        print("Ваше имя и данные успешно удалены!")
    except:
        print("Пользователя с таким именем не существует!")

def quit_user():
    quit()

ACTIONS = {
    1: list_users,
    2: create_user,
    3: read_user,
    4: update_user,
    5: delete_user,
    6: quit_user,
}

def select_action(answer: int):
    return ACTIONS.get(answer, show_menu)

def main():
    answer = 0
    while True:
        action = select_action(answer)
        answer = action()

main()