try:

    num = eval(input("prompt a number"))
    for i in range(10):
        if num > 9:
            print("The number is greater")
        if num < 0:
            print("The number is lower")
except ValueError:
    print("The game is over")
try:
    name = input()
    gender = input("prompt")
    age = input("input your age ")
    if name == "":
        name = None
    elif 18 > age > 30:
        age = None
except ValueError:
    print("Your information is stored")
