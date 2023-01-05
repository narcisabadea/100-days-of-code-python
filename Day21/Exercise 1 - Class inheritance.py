# The process of inheriting behaviour from an existing class = Class inheritance
# Can inherit both atributes and methods (appearance and behaviour)
# To add the inheritance from another class we just add a set of parantheses after the name of the class and insert the class from which we want to inherit from
# To get in hold of everything from that class we need to add the super() class

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater")

    def swim(self):
        print('Moving in water')


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
