import math


def getSqrt(number):
    if number < 0:
        raise Exception("The number is lower than 0")
    return math.sqrt(number)


alpha = input("Prompt a number")
try:
    number = float(alpha)
    print(getSqrt(number))
except ValueError as identifier:
    print("The number is not valid")
