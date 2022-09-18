#Request of necessary data from user and notification.
print("Welcom to your robot's control menu. Here you can insert direction and quantity of steps for your robot.\
 Length of one step is 100 cm. Robot can move up, down, left and right. To insert direction and quantity of steps\
 please use a short comand:'u', 'd', 'l' or 'r' and after space insert quantity of steps ('u', 'd', 'l', or 'r' ->\
 space -> q-ty of steps). To cancel the insert field please push 'enter' or insert 'q' and push 'enter'.")
steps = {
    'u':0,
    'd':0,
    'l':0,
    'r':0,
}
while True:
    data_request = input("Please insert direction and quantity of steps using space button:")
    try:
        data_request_list = data_request.split()
        if data_request_list[0] == 'q' or data_request_list[0] == '':
            break
        command = data_request_list[0]
        command_value = int(data_request_list[-1])
        steps[command] = steps[command] + command_value
    except:
        print("Please insert data as it is discribed at the very beggining. ('u', 'd', 'l', or 'r' -> space -> q-ty of steps)")
# Calculation of robot's route.
import math
length_route = math.sqrt((steps['u']**2 - steps['d']**2) + (steps['r']**2 - steps['l']**2))
length_route_round = round(length_route)
print(f"Your robot's route is {length_route_round} meters.")