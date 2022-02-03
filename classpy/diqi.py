import datetime
import random

number = input("prompt a number: ")


def typing():
    if type(number) == int:
        print("the nunmber {} is an int".format(number))
    elif type(number) == float:
        print("The number {} is a float".format(number))
    elif type(number) == float:
        print("The number {} is a float".format(number))
    else:
        print("not")


typing()

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
print(x.strftime("%x"))
print(x.strftime("%H"))
print(x.strftime("%Y"))
print(x.strftime("%b"))
print(x.strftime("%M"))
print(x.strftime("%z"))
p = datetime.datetime.now()
print(p.year)
print(p.strftime("%A"))


def ran():
    random.random(number)
