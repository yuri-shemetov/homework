import datetime
import os
from time import sleep
from digits import one, two, three, four, five, six, seven, eight, nine, zero

def time():
    numbers = {}
    
    time_now = datetime.datetime.now()
    str_time = time_now.strftime("%H %M %S")
    
    for k, v in enumerate(str_time, start = 1) :
        numbers[k] = v
    
    return numbers

def symbols():
    numbers = time()
    for i in range(5):
        string = "\u0020"
        space = "\u0020"
        point = "\u25EF"
        for value in numbers.values():
            if value == '1': 
                string += space + one[i]
            if value == '2':
                string += space + two[i]
            if value == '3': 
                string += space + three[i]
            if value == '4': 
                string += space + four[i]
            if value == '5': 
                string += space + five[i]
            if value == '6': 
                string += space + six[i]
            if value == '7': 
                string += space + seven[i]
            if value == '8': 
                string += space + eight[i]
            if value == '9': 
                string += space + nine[i]
            if value == '0': 
                string += space + zero[i]
            # Вывод мигающих точек
            if value == space and i%2 != 0 and int(numbers[8])%2 != 0:
                string += point + 2*space
            elif value == space and i%2 != 0 and int(numbers[8])%2 == 0:
                string += 3*space
            else:    
                string += 3*space                           
        print(string)

def main():
    while True:
        output = symbols()
        sleep(1)
        os.system("cls")
        
main()