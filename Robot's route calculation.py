#Request of necessary data from user and notification.
print("Welcom to your robot's control menu. Here you can insert direction and quantity of steps for your robot.\
 Length of one step is 1m. Robot can move up, down, left and right. To insert direction and quantity of steps\
 please use a short comand:'u', 'd', 'l' or 'r' and after space insert quantity of steps ('u', 'd', 'l', or 'r' ->\
 space -> q-ty of steps). To cancel the insert field please insert 'q' and push 'enter'.")
steps = {
    'u':0,
    'd':0,
    'l':0,
    'r':0,
}
while True:
    data_request = input("Please insert direction and quantity of steps using space button:")
# Splitting input data and ending the cycle with "q".
    try:
        data_request_list = data_request.split()
        if data_request_list[0] == 'q':
            break
# Checking value of steps (if it's valid - positive number) and ending the cycle if value is not valid.
        elif int(data_request_list[1]) < 0:
            print("Quantity of steps must be a positive number!")
            break
# Making the list with input data.
        command = data_request_list[0]
        command_value = int(data_request_list[-1])
        steps[command] = steps[command] + command_value
#Printing the message if input data is not valid. 
    except:
        print("Please insert data as it is discribed at the very beggining. ('u', 'd', 'l', or 'r' -> space -> q-ty of steps)")\
# Calculation of robot's route.
import math
length_route = math.sqrt((steps['u'] - steps['d'])**2 + (steps['r'] - steps['l'])**2)
length_route_round = round(length_route)
print(f"Your robot's route is {length_route_round} meters.")