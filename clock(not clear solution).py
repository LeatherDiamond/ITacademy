import datetime
import time
import os
numbers = {
     '0': ['XXXX',
           'X  X',
           'X  X',
           'X  X',
           'XXXX'],
     '1': [' XX ',
           '  X ',
           '  X ',
           '  X ',
           'XXXX'],
     '2': ['XXXX',
           '   X',
           'XXXX',
           'X   ',
           'XXXX'],
     '3': ['XXXX',
           '   X',
           'XXXX',
           '   X',
           'XXXX'],
     '4': ['X  X',
           'X  X',
           'XXXX',
           '   X',
           '   X'],
     '5': ['XXXX',
           'X   ',
           'XXXX',
           '   X',
           'XXXX'],
     '6': ['XXXX',
           'X   ',
           'XXXX',
           'X  X',
           'XXXX'],
     '7': ['XXXX',
           '   X',
           '   X',
           '   X',
           '   X'],
     '8': ['XXXX',
           'X  X',
           'XXXX',
           'X  X',
           'XXXX'],
     '9': ['XXXX',
           'X  X',
           'XXXX',
           '   X',
           'XXXX'],
     ':': [' X  ',
           ' X  ',
           ' X  ',
           ' X  ',
           ' X  '],
}
#Creating a function and a cycle.
while True:
    def main():
        cdt = datetime.datetime.now().time()
        cdt = cdt.strftime("%H:%M:%S")
# Clearing the console.
       
#Printing clock with modified symbols (string by string).
        l1 = ''
        l2 = ''
        l3 = ''
        l4 = ''
        l5 = ''
        for i in cdt:
            l1 = l1 + '  ' + numbers[i][0]
            l2 = l2 + '  ' + numbers[i][1]
            l3 = l3 + '  ' + numbers[i][2]
            l4 = l4 + '  ' + numbers[i][3]
            l5 = l5 + '  ' + numbers[i][4]
        print(l1[0:14] + l1[15:32] + l1[33:])
        print(l2[0:15] + l2[16:33] + l2[34:])
        print(l3[0:15] + l3[16:33] + l3[34:])
        print(l4[0:15] + l4[16:33] + l4[34:])
        print(l5[0:15] + l5[16:33] + l5[34:])
        time.sleep(0.1)
        os.system('cls')
        print(l1[0:15] + l1[16:33] + l1[34:])
        print(l2[0:14] + l2[15:32] + l2[33:])
        print(l3[0:15] + l3[16:33] + l3[34:])
        print(l4[0:15] + l4[16:33] + l4[34:])
        print(l5[0:15] + l5[16:33] + l5[34:])
        time.sleep(0.1)
        os.system('cls')
        print(l1[0:15] + l1[16:33] + l1[34:])
        print(l2[0:15] + l2[16:33] + l2[34:])
        print(l3[0:14] + l3[15:32] + l3[33:])
        print(l4[0:15] + l4[16:33] + l4[34:])
        print(l5[0:15] + l5[16:33] + l5[34:])
        time.sleep(0.1)
        os.system('cls')
        print(l1[0:15] + l1[16:33] + l1[34:])
        print(l2[0:15] + l2[16:33] + l2[34:])
        print(l3[0:15] + l3[16:33] + l3[34:])
        print(l4[0:14] + l4[15:32] + l4[33:])
        print(l5[0:15] + l5[16:33] + l5[34:])
        time.sleep(0.1)
        os.system('cls')
        print(l1[0:15] + l1[16:33] + l1[34:])
        print(l2[0:15] + l2[16:33] + l2[34:])
        print(l3[0:15] + l3[16:33] + l3[34:])
        print(l4[0:15] + l4[16:33] + l4[34:])
        print(l5[0:14] + l5[15:32] + l5[33:])
        time.sleep(0.1)
        os.system('cls')
        print(l1[0:15] + l1[16:33] + l1[34:])
        print(l2[0:15] + l2[16:33] + l2[34:])
        print(l3[0:15] + l3[16:33] + l3[34:])
        print(l4[0:14] + l4[15:32] + l4[33:])
        print(l5[0:15] + l5[16:33] + l5[34:])
        time.sleep(0.1)
        os.system('cls')
        print(l1[0:15] + l1[16:33] + l1[34:])
        print(l2[0:15] + l2[16:33] + l2[34:])
        print(l3[0:14] + l3[15:32] + l3[33:])
        print(l4[0:15] + l4[16:33] + l4[34:])
        print(l5[0:15] + l5[16:33] + l5[34:])
        time.sleep(0.1)
        os.system('cls')
        print(l1[0:15] + l1[16:33] + l1[34:])
        print(l2[0:14] + l2[15:32] + l2[33:])
        print(l3[0:15] + l3[16:33] + l3[34:])
        print(l4[0:15] + l4[16:33] + l4[34:])
        print(l5[0:15] + l5[16:33] + l5[34:])
        time.sleep(0.1)
        os.system('cls')
        print(l1[0:14] + l1[15:32] + l1[33:])
        print(l2[0:15] + l2[16:33] + l2[34:])
        print(l3[0:15] + l3[16:33] + l3[34:])
        print(l4[0:15] + l4[16:33] + l4[34:])
        print(l5[0:15] + l5[16:33] + l5[34:])
        time.sleep(0.1)
        os.system('cls')
    main()