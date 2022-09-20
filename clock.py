#Import of necessary libraries.
import datetime
import time
import os
#Drawing of numbers for clock.
zero = """
⬛⬛⬛⬛
⬛    ⬛
⬛    ⬛
⬛    ⬛
⬛⬛⬛⬛"""
one = """
⬛⬛
  ⬛
  ⬛
  ⬛
⬛⬛⬛"""
two = """
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛
⬛
⬛⬛⬛⬛"""
three = """
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛"""
four = """
⬛    ⬛
⬛    ⬛
⬛⬛⬛⬛
      ⬛
      ⬛"""
five = """
⬛⬛⬛⬛
⬛
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛"""
six = """
⬛⬛⬛⬛
⬛
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛"""
seven = """
⬛⬛⬛⬛
      ⬛
      ⬛
      ⬛
      ⬛"""
eight = """
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛"""
nine = """
⬛⬛⬛⬛
⬛    ⬛
⬛⬛⬛⬛
      ⬛
⬛⬛⬛⬛"""
while True:
#Import of current time.
    cdt = datetime.datetime.now()
#Transformation of current date and time to necessary format (Hours, Minutes and Seconds).
    cdt = cdt.strftime("%H:%M:%S")
    time.sleep(0.2)
#Clearing the console.
    os.system('cls') 
    print(cdt)
