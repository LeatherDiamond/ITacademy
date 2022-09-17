#Login request.
input = str(input("Insert your login:"))
#Decorator.
def account_balance(func):
    def wrapper_decorator(*args, **kwargs):
        if input != 'admin':
            return'Access denied!'
        value = func(*args, **kwargs)
        return value
    return wrapper_decorator
#Applying decorator to the main function.
@account_balance
def balance():
    return'Your account balance is 5789 USD.'
#Launching the function with decorator.
funct_launch = balance()
print(funct_launch)
