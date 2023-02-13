# Decorator function as a function that's going to give additional functionality to an existing function.
# Python functions are known as first-class objects,  which basically means that you can pass a function around as an argument, just like what you could do with an integer, a string or a float, it's treated
# identically.
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


# The @ is only syntactic sugar that replaces these lines
decorated_function = delay_decorator(say_greeting)
decorated_function()
