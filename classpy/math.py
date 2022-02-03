import math

number = input("Input a number")
try:
    number = float(number)
    print(math.sqrt(number))
    print("This part is done")

except Exception as identifier:
    print(identifier)
print("The end")
