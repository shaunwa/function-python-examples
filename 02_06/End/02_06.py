def divide(x, y):
    return x / y

def second_argument_isnt_zero(func):
    def safe_version(*args):
        if args[1] == 0:
            print('Warning: second argument is zero')
            return
        return func(*args)

    return safe_version

divide_safe = second_argument_isnt_zero(divide)

print(divide_safe(10, 2))