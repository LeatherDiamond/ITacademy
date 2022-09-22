#Import of necessary libraries.
from datetime import datetime
from operator import itemgetter
import time
import os
#Drawing of numbers for clock.
time_numbers ={
    0: """
⬛⬛⬛⬛
⬛    ⬛
⬛    ⬛
⬛    ⬛
⬛⬛⬛⬛""",
    1: """
 ⬛⬛   
   ⬛   
   ⬛   
   ⬛   
 ⬛⬛⬛ """,
    2: """
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛
⬛      
⬛⬛⬛⬛""",
    3: """
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛""",
    4: """
⬛    ⬛
⬛    ⬛
⬛⬛⬛⬛
      ⬛
      ⬛""",
    5: """
⬛⬛⬛⬛
⬛      
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛""",
    6: """
⬛⬛⬛⬛
⬛      
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛""",
    7: """
⬛⬛⬛⬛
      ⬛
      ⬛
      ⬛
      ⬛""",
    8: """
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛""",
    9: """
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛""",
}

zero = """
⬛⬛⬛⬛
⬛    ⬛
⬛    ⬛
⬛    ⬛
⬛⬛⬛⬛"""


def format_share_time(time_str):
    output_numbers = []
    conver_to_list = []
    try:
        for i in time_str:
            output_numbers.append(time_numbers[int(i)])
    except:
        print('Error!')
    for i in output_numbers:
        conver_to_list.append(i.split('\n'))
    return conver_to_list


while True:
    cdt = datetime.now()
    cdt = cdt.strftime("%H:%M:%S")
    share_time = cdt.replace(':', '')
    list_time = format_share_time(share_time)
    for i in list_time:
        result = []
        for j in range(len(i)):
            result.append(list(map(itemgetter(j), list_time)))
        for d in result:
            print(*d)
        break
    
    time.sleep(1)
    os.system('cls')
