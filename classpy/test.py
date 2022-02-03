try:
    alpha = float(input())
    beta = float(input())
    print("the beta:{.2f}".format(alpha / beta))
    print("alpha:{.2f}".format(alpha * beta))


except ZeroDivisionError:
    print("Zero can't be divided")
except ValueError:
    print("There are some bugs")
print("The program has been executed")
