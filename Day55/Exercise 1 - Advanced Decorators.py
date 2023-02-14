# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {sum(args)}")
    return wrapper

# Use the decorator 👇


@logging_decorator
def a_function(a, b, c):
    return a+b+c


a_function(1, 2, 3)
