import types


class Person(object):
    def __init__(self, name):
        self.name = name

    def sing(self):
        print(self.name + " can sing a song ")


def walk(self):
    print(self.name + " can walk around")


diallo = Person("AlphaOumar")
diallo.sing()
diallo.walk = types.MethodType(walk, diallo)
# diallo.walk()
