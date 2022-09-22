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
#Function to create lists with accordance to current data and adding to the list that will be made by drawed before numbers.
def format_share_time(time_str):
    output_numbers = []
    conver_to_list = []
    try:
        for i in time_str:
            output_numbers.append(time_numbers[i])
    except:
        print('Error!')
    for i in output_numbers:
        conver_to_list.append(i.split('\n'))
    return conver_to_list

#Function to replace emoty separator from dictionary to black squares.
def replace_string(string_for_replace):
    result = string_for_replace
    result[2] = '⬛'
    result[5] = '⬛'
    return result
#Making a circle with time import and creation of a list with time data ready for print.
while True:
    cdt = datetime.now()
    cdt = cdt.strftime("%H:%M:%S")
    list_time = format_share_time(cdt)
    for i in list_time:
        result = []
        for j in range(len(i)):
            result.append(list(map(itemgetter(j), list_time)))
        def unpack(s):
            return " ".join(map(str, s))
        clean_result = result[1:]
#Printing separator down->top.
        os.system('cls')
        print(f'{unpack(clean_result[0])}\n{unpack(clean_result[1])}\n{unpack(clean_result[2])}\n{unpack(clean_result[3])}\n{unpack(replace_string(clean_result[4]))}\n')
        time.sleep(0.2)
        os.system('cls')
        print(f'{unpack(clean_result[0])}\n{unpack(clean_result[1])}\n{unpack(clean_result[2])}\n{unpack(replace_string(clean_result[3]))}\n{unpack(clean_result[4])}\n')
        time.sleep(0.2)
        os.system('cls')
        print(f'{unpack(clean_result[0])}\n{unpack(clean_result[1])}\n{unpack(replace_string(clean_result[2]))}\n{unpack(clean_result[3])}\n{unpack(clean_result[4])}\n')
        time.sleep(0.2)
        os.system('cls')
        print(f'{unpack(clean_result[0])}\n{unpack(replace_string(clean_result[1]))}\n{unpack(clean_result[2])}\n{unpack(clean_result[3])}\n{unpack(clean_result[4])}\n')
        time.sleep(0.2)
        os.system('cls')
        print(f'{unpack(replace_string(clean_result[0]))}\n{unpack(clean_result[1])}\n{unpack(clean_result[2])}\n{unpack(clean_result[3])}\n{unpack(clean_result[4])}\n')
        time.sleep(0.2)
        os.system('cls')
#Printing separator up->down.
        print(f'{unpack(replace_string(clean_result[0]))}\n{unpack(clean_result[1])}\n{unpack(clean_result[2])}\n{unpack(clean_result[3])}\n{unpack(clean_result[4])}\n')
        time.sleep(0.2)
        os.system('cls')
        print(f'{unpack(clean_result[0])}\n{unpack(replace_string(clean_result[1]))}\n{unpack(clean_result[2])}\n{unpack(clean_result[3])}\n{unpack(clean_result[4])}\n')
        time.sleep(0.2)
        os.system('cls')
        print(f'{unpack(clean_result[0])}\n{unpack(clean_result[1])}\n{unpack(replace_string(clean_result[2]))}\n{unpack(clean_result[3])}\n{unpack(clean_result[4])}\n')
        time.sleep(0.2)
        os.system('cls')
        print(f'{unpack(clean_result[0])}\n{unpack(clean_result[1])}\n{unpack(clean_result[2])}\n{unpack(replace_string(clean_result[3]))}\n{unpack(clean_result[4])}\n')
        time.sleep(0.2)
        os.system('cls')
        print(f'{unpack(clean_result[0])}\n{unpack(clean_result[1])}\n{unpack(clean_result[2])}\n{unpack(clean_result[3])}\n{unpack(replace_string(clean_result[4]))}\n')
        time.sleep(0.2)
        os.system('cls')
        break
    
