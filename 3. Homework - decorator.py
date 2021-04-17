login = input("Введите имя пользователя: ")
login = login.lower()

def check_user(func):
    def wrapper_decorator(*args, **kwargs):
        if args == ('admin',):
            return func(*args, **kwargs)
        return f'К сожалению, {login.title()}, вам доступ запрещен!'
    return wrapper_decorator
    
@check_user
def the_amount(name):
    """
    Возвращает сумму со счета администратора 
    """
    return ('Ваша сумма на счете: 1_000_000 $')

print(the_amount(login))