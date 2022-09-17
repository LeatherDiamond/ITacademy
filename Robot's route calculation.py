#Request of necessary data from user and notification.
print("Welcom to your robot's control menu. Here you can insert direction and quantity of steps for your robot.\
Length of one step is 100 cm. Robot can move up, down, left and right. To insert direction and quantity of steps\
please use a short comand:'u', 'd', 'l' or 'r' and after space insert quantity of steps ('u', 'd', 'l', or 'r' ->\
 space -> q-ty of steps). To cancel the insert field please push 'enter' or insert 'q' and push 'enter'.")
while True:
    data_request = str(input("Please insert direction and quantity of steps using space button:"))
    if data_request == '' or data_request == 'q':
        break
    elif data_request is not str('u') + str(' ') + str(int[0:]):
        break