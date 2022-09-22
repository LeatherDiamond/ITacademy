#Import of necessary libraries.
from datetime import datetime
from operator import itemgetter
import time
import os
#Drawing of numbers for clock.
time_numbers = {
    '0': """
⬛⬛⬛⬛
⬛    ⬛
⬛    ⬛
⬛    ⬛
⬛⬛⬛⬛""",
    '1': """
 ⬛⬛   
   ⬛   
   ⬛   
   ⬛   
 ⬛⬛⬛ """,
    '2': """
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛
⬛      
⬛⬛⬛⬛""",
    '3': """
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛""",
    '4': """
⬛    ⬛
⬛    ⬛
⬛⬛⬛⬛
      ⬛
      ⬛""",
    '5': """
⬛⬛⬛⬛
⬛      
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛""",
    '6': """
⬛⬛⬛⬛
⬛      
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛""",
    '7': """
⬛⬛⬛⬛
      ⬛
      ⬛
      ⬛
      ⬛""",
    '8': """
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛""",
    '9': """
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛""",
    ':': """
  
  
  
  
  """
}


def format_share_time(time_str):
#Function to create lists with accordance to current data and adding to the list that will be made by drawed before numbers.'''
    output_numbers = []
    conver_to_list = []
    try:
        for i in time_str:
            output_numbers.append(time_numbers[i])
    except:
        print('Fuck')
    for i in output_numbers:
        conver_to_list.append(i.split('\n'))
    return conver_to_list


def replace_string(string_for_replace):
#Function to replace emoty separator from dictionary to black squares.
    result = string_for_replace
    result[2] = '⬛'
    result[5] = '⬛'
    return result


def unpack(s):
#Function to unpack printed strings in the end.
    return " ".join(map(str, s))



def check_time():
#Function to insert current time from the system.
    cdt = datetime.now()
    cdt = cdt.strftime("%H:%M:%S")
    list_time = format_share_time(cdt)
    last_result = []
    for i in list_time:
        result = []
        for j in range(len(i)):
            result.append(list(map(itemgetter(j), list_time)))
        clean_result = result[1:]

        last_result += clean_result
        break

    return last_result


while True:
#Cicle to print time with drawed numbers and moving separator.
    clean_result = check_time()
    os.system('cls')
    print(f'{unpack(check_time()[0])}\n{unpack(check_time()[1])}\n{unpack(check_time()[2])}\n{unpack(check_time()[3])}\n{unpack(replace_string(check_time()[4]))}\n')
    time.sleep(0.2)
    os.system('cls')
    print(f'{unpack(check_time()[0])}\n{unpack(check_time()[1])}\n{unpack(check_time()[2])}\n{unpack(replace_string(check_time()[3]))}\n{unpack(check_time()[4])}\n',)
    time.sleep(0.2)
    os.system('cls')
    print(f'{unpack(check_time()[0])}\n{unpack(check_time()[1])}\n{unpack(replace_string(check_time()[2]))}\n{unpack(check_time()[3])}\n{unpack(check_time()[4])}\n',)
    time.sleep(0.2)
    os.system('cls')
    print(f'{unpack(check_time()[0])}\n{unpack(replace_string(check_time()[1]))}\n{unpack(check_time()[2])}\n{unpack(check_time()[3])}\n{unpack(check_time()[4])}\n',)
    time.sleep(0.2)
    os.system('cls')
    print(f'{unpack(replace_string(check_time()[0]))}\n{unpack(check_time()[1])}\n{unpack(check_time()[2])}\n{unpack(check_time()[3])}\n{unpack(check_time()[4])}\n')
    time.sleep(0.2)
    os.system('cls')
    print(f'{unpack(check_time()[0])}\n{unpack(replace_string(check_time()[1]))}\n{unpack(check_time()[2])}\n{unpack(check_time()[3])}\n{unpack(check_time()[4])}\n')
    time.sleep(0.2)
    os.system('cls')
    print(f'{unpack(check_time()[0])}\n{unpack(check_time()[1])}\n{unpack(replace_string(check_time()[2]))}\n{unpack(check_time()[3])}\n{unpack(check_time()[4])}\n')
    time.sleep(0.2)
    os.system('cls')
    print(f'{unpack(check_time()[0])}\n{unpack(check_time()[1])}\n{unpack(check_time()[2])}\n{unpack(replace_string(check_time()[3]))}\n{unpack(check_time()[4])}\n')
    time.sleep(0.2)
    
