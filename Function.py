# import Class
import File


def my_function(name):
    print(name)


my_function("The username is Diallo")


def alphaoumar(*me):
    print("Is the second element of tuple ", me[1])


alphaoumar("good", "smile", "will")


def oumar(first, second, third):
    print(f"The first value is {first}, second {second}, third {third}")


oumar(7, 4, 34)
try:
    def sia(al):
        print("alpha oumar diallo", al, "its name")
        sia("diallo")
except TypeError:
    print("There is an error ")
finally:
    print("It's well done!")


def funtions():
    numbers = input("Prompt a number")
    if numbers > 10:
        return numbers
        print("The number is great than 0")
    else:
        return -numbers
        print("The number is negative")


def greetting(greet, person):
    print(greet, person)


greetting("Hey ", "Diallo")
print(greetting("Morning", "Alpha oumar diallo"))


def multiple(*names):
    print("The name", names)


multiple("all", "oumar", 21, "dialo", [23, 43, 435, 54, ])


def factorial(lam):
    if lam == 1:
        return 1
    elif lam > 1:
        return lam * factorial(lam - 1)
    else:
        return lam * factorial(lam + 1)


number = 3
print("The factorial of the number is ", number, factorial(number))

# Using the recursive function
try:
    def recursor():
        recursor()
except File:
    recursor()
finally:
    print("None")
# Lambda function

abdoul = lambda: print("Welcome to the lambda function")
abdoul()
abdoul = lambda diallo: diallo * 23
print(abdoul(3))

lists = [432, 5, 5334, 463, 765, 2, 645, 6, 4, 23, 76, 6, 789, 0, 545, 45, 34, 74, 23, 7, 8, 9, 3]
the_new = list(map(lambda alpha: alpha * 2, lists))
print(the_new)

# The scope of the variable
global_variable = "Alpha oumar Diallo"
globo = 34  # global vairiable
alpha = 39


def vari():
    print("That is a global variable", global_variable * 3)
    the = 3  # is a local variable
    print(the)
    return globo - the


def variableinner():
    print("That is a global variableinner", )
    bien = "The smile"  # is a local variable
    print(bien)
    return globo-alpha


variableinner()

vari()
print(global_variable)


