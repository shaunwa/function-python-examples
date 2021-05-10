def combine(x, y, op):
  return op(x, y)

def add(x, y):
  return x + y
  
def subtract(x, y):
  return x - y

def polynomial(x, y):
  return 2 * x * x + 3 * y


def create_printer():
  def printer():
    print('Hello functional!')

  return printer

# def double(x):
#   return x * 2

# def triple(x):
#   return x * 3

# def quadruple(x):
#   return x * 4

def create_multiplier(y):
  def multiplier(x):
    return x * y

  return multiplier

#############################

def create_arg_checker(arg_check_func, warning_message):
  def arg_checker(func):
    def safe_version(*args, **kwargs):
      if arg_check_func(*args, **kwargs):
        print(f'ARGS: {warning_message}')
        return

      return func(*args, **kwargs)

    return safe_version

  return arg_checker

def second_arg_zero(*args):
  return args[1] == 0;

def first_arg_gt_100(*args):
  return args[0] > 100

@create_arg_checker(second_arg_zero, 'Warning: second arg is zero!')
@create_arg_checker(first_arg_gt_100, 'Warning: first arg is greater than 100')
def divide(x, y):
  return x / y

def name_is_lt_2_chars(*args, **kwargs):
  return len(kwargs['name']) < 2

@create_arg_checker(name_is_lt_2_chars, 'Warning: name arg must be longer than 2 chars')
def create_person(name, age):
  return {
    'name': name,
    'age': age,
  }
