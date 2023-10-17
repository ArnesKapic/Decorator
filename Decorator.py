def hello_decorator(func):
    def wrapper():
        for _ in range(2):
            func()
    return wrapper


def function_hello():
    print("Hello")


function_being_used = hello_decorator(function_hello)

function_being_used()
