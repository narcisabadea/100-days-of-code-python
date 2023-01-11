# *args used to add many positional arguments
# returns a tuple

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 3, 5, 7, 9))

# **kwargs used to add many keyword arguments
# returns a dictionary


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make") # get is used too retrieve the value and if the value was not provided then it returns None
        self.model = kwargs.get("model")
        # self.make = kwargs["make"] # if the value was not provided then it will throw an error
        # self.model = kwargs["model"]


myCar = Car(make="Nissan")
print(myCar.model)
