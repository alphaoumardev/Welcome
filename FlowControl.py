# We are going to use the flow control in this scope
alpha = 35
if alpha > 30:
    if alpha >= 40:
        print("That means it's over 30")  # Notice that we can nest the (if)statement by the way
    elif alpha == 35:  # and notice in python the (elif)statement is the else if of the other languages
        # it's just it syntax is different from the others
        print("He's also adult by the way")
    else:
        print("Dont mind about that person age ")
    print("is a number under 30 age ")
elif alpha == 21:
    print("That is My exact age at the moment")
elif alpha < 10:
    print("His age is under 10")
else:
    print("His is an adult")
# The loop statements for
number_list = [23, 4, 50, 36, 65, 23, 56, ]
suma = 0
substraction = 0
multiple = 1
for val in number_list:
    suma = val + suma
    print("The sum of the number_list is ", suma)
    substraction = val - substraction
    if substraction >= 23:
        print("The substraction of the number_list is", substraction)
        break
else:
    multiple = val * multiple
    print("The multiple of the number_list is going to be ", multiple)

    for val in number_list:
        suma = val + suma
        print("The sum of the number_list is ", suma)
        substraction = val - substraction
        if substraction >= 23:
            print("The substraction of the number_list is", substraction)
            continue
    else:
        # multiple = val * multiple
        print("The multiple of the number_list is going to be ", multiple)

# Using range() function to determine the start, stop, and end of the loop
print(range(10))
print(list(range(10)))
print(list(range(1, 25, 6)))
print(list(range(20, 100)))
print("The tuple of range", tuple(range(10, 50)))

if number_list[2] == 50:
    print(number_list[2], " Is the exact value")

elif number_list[2] <= 15:
    print("That is not the second element of the list")
else:
    print("The list number has no 50 as element")

    # The while loop  in sum
    n = 200
    i = 110
    dia = 0
    while i <= n:
        dia = dia + 1
        i = i + 1
        print("The sum", dia)
number_list.append(16)
lis = number_list.copy()  # 同成品油to copy a list from another one using the copy()
# oumar=list(number_list)# to copy a list by using the list()method
print(number_list)
print("The length of the list is ", len(number_list))  # the length of the list
number_list.remove(number_list[5])
print("The length of the list is ", len(number_list))
del number_list[2]  # deleting an element of the list by using the [del]
print("The length of the list is ", len(number_list))
oumar = number_list + lis  # add a list in to another
number_list.pop()  # to remove one element
print("The length of the list is ", len(number_list))
print(number_list)

for diallo in number_list:  # to add the list in to the second
    lis.append(diallo)
    print("using for loop", lis)
    # OR
    lis.extend(number_list)
    print("using  extend ", lis)

number_list.clear()  # To clear the entire list
print("AFTER RREMOVING BY THE function clear() is going to be:")
print("Now the length of the list is ", len(number_list))
print("The COPY list is =:) ", lis)  # the copy list
print("The new COPY list is =:) ", oumar)  # the copy list

for al in "Alpha ooumar diallo":
    if al == "r":
        pass
        # break
        print("To use the break in a loop ", al)
    elif al == "h":
        continue
    else:
        print("These parameters are not applicable in this scope", al)

me = 13
you = 57
print("A") if me > you else print("B")
