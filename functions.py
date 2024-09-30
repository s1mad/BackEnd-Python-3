'''
    Функции и лямбды для лабараторной №3
'''

def greet():
    '''Функция без параметров'''
    return "Hello, World!"

def add(a, b):
    '''Функция с параметрами'''
    return a + b

def introduce(name, age=18):
    '''Функция с несколькими параметрами со значениями по умолчанию'''
    return f"My name is {name} and I am {age} years old."

def multiply(a: int, b: int) -> int:
    '''Функция с несколькими параметрами, у которых задан тип'''
    return a * b

def sum_all(*args):
    '''Функция с неопределённым количеством параметров (args)'''
    return sum(args)

def print_person_info(**kwargs):
    '''Функция с неопределённым количеством параметров (kwargs)'''
    return f"Name: {kwargs.get('name')}, Age: {kwargs.get('age')}"

def outer_function():
    '''Функция, вызывающая внутри себя другую функцию'''
    def inner_function():
        return "Inner function called!"
    return inner_function()

def apply_function(func, value):
    '''Функция, принимающая функцию как параметр (пример 1)'''
    return func(value)

def modify_string(func, string):
    '''Функция, принимающая функцию как параметр (пример 2)'''
    return func(string.upper())

def operate_on_list(func, values):
    '''Функция, принимающая функцию как параметр (пример 3)'''
    return [func(value) for value in values]

def create_multiplier(n):
    '''Функция с объявленной внутри локальной функцией (пример 1)'''
    def multiplier(x):
        return x * n
    return multiplier

def power_function(exp):
    '''Функция с объявленной внутри локальной функцией (пример 2)'''
    def power(x):
        return x ** exp
    return power

# Лямбда-выражение без параметров
no_param_lambda = lambda: "Lambda without params"

# Лямбда-выражение с параметрами
sum_lambda = lambda a, b: a + b

def apply_lambda(lambda_func, value):
    '''Функция, принимающая лямбда-выражение как параметр'''
    return lambda_func(value)

def closure_counter():
    '''Функция с замыканием (пример 1)'''
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

def make_adder(x):
    '''Функция с замыканием (пример 2)'''
    def adder(y):
        return x + y
    return adder

def store_values():
    '''Функция с замыканием (пример 3)'''
    values = []
    def add_value(value):
        values.append(value)
        return values
    return add_value
