print("welcome to first program in python")
# That is the comment in python
""" Notice That in python there's no semi-colon and
"""
alpha = 5
print(alpha)
print("diallo")
diallo = ["alpha", "oumar", "diallo"]  # list
print(type(diallo))
oumar = alpha + 2j  # this is a complex number or variable
print("the type of oumar is ", type(oumar))
alpha = 23.4
print(alpha, " is a ", type(alpha))
diallo = [542, 544, 523, 5, 46, 23, 43, 543, 541, 12576, 56]
print(diallo[5])  # to print the fith(5) element of the list
print(diallo[2:9])  # to print the intervalle from second element to the nigth(9)elementof the list

tuples = ("alpha", "oumar", "diallo", 21, 2)  # is the declaration of tuples that are sequence and can't be modified
print("The second element of the tuple is " + tuples[2])
print(tuples[1:3])

stringing = "Is this the using string in python?  Yes it is"
print(stringing)

toSet_type = {43, 54, 65, 7623, 9, 0, 34}  # The setting data type
print(toSet_type, " is the set data type ", type(toSet_type))

dictionary_type = {"alpha": 20, 22: "to_next_month"}
print(dictionary_type, type(dictionary_type))
"""To convert a datatype we can use a function as float(...),int(...)..."""
al = {"name": "hele", "detail": [{"age": 18, "job": "tester"}, "man"]}
print(al["detail"][1][2])

# coversion
a = 33
b = "43"
print(type(a), type(b))
b = int(b)
print("The sum = ", a + b)

liste = [2 ** x for x in range(100)]
print(liste, "\t")
