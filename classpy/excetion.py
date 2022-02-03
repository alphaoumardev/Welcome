try:
    name="alphaoumar diallo"
    index=eval(input("Please input a number"))
    print(name[index])

except IndexError:
    print(" the identifier:")
except TypeError:
    print("type error")
except Exception:
    print("Here is the exception")
else:
    print("Here is the elese")
finally:
    print("The final point")