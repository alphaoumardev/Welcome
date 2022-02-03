class Dad:
    alpha = 21

    def __init__(self):
        print("That is the dad class")
        self.price = 10
    print(alpha)

    def you(self):
        print(f"You belong to the dad class {self.price}")

    def max(self, maxprice):
        self.price = maxprice


me = Dad()
me.you()
me.price = 100
me.you()


# me.price(23)
# me.you()
def he():
    print("He belong to the mom class")


class Mon(Dad):
    def __init__(self):
        super().__init__()
        print("The mom class")


a = Mon()
he()


class Person(Mon):
    def __init__(self, fname, lname):
        super().__init__()
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


oumar = Student("Mike", "Olsen", 2023)
oumar.welcome()


class Ason(Mon):
    def __init__(self, mes="Alpha", sister="oumardiallo"):
        self.me = mes
        self.sister = sister
        super().__init__()

    def toShow(self):
        print(self.me, self.sister)


son = Ason()
son.toShow()
