🧱 Python Decorator Example

This simple Python script demonstrates how function decorators work in Python by using a hello_decorator that modifies another function to execute twice.
🚀 Overview

In this program:

    A decorator function named hello_decorator is defined.

    It takes a function as input, wraps it inside another function (wrapper), and returns the new behavior.

    The wrapped function (function_hello) is then called — but instead of printing "Hello" once, it prints it twice, thanks to the decorator.

📜 Code Example

def hello_decorator(func):
    def wrapper():
        for _ in range(2):
            func()
    return wrapper

def function_hello():
    print("Hello")

function_being_used = hello_decorator(function_hello)

function_being_used()

🧠 Output:

Hello
Hello

📌 Key Concepts

    Decorator: A function that takes another function as an argument and extends or alters its behavior.

    Higher-order function: A function that takes another function as input or returns one.

    Wrapper function: The inner function that defines the new behavior before calling the original function.

🛠️ How to Run

    Save the script in a .py file, for example decorator_example.py

    Run it with Python:

python decorator_example.py

🔄 Next Steps

You can expand this by:

    Using the @ syntax for decorators

    Adding arguments to the decorated function

    Creating reusable decorators for logging, timing, access control, etc.
