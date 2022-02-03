# 3、编程实现：用列表实现一个简单的队列（队列的特点“先进先出”）
# lists=[0,545,45,34,74,23,7,8,9,3]
lists = [432, 5, 5334, 463, 765, 2, 645, 6, 4, 23, 76, 6, 789, 0, 545, 45, 34, 74, 23, 7, 8, 9, 3]
lists.pop(0)
print(lists)
lists.append([2, 4])
print(lists)
# lists.extend(2)
print(lists)
lists.remove(4)
print(lists)
lists.reverse()
newList = list(map(lambda alpha: alpha * 2, lists))
print(newList)
diallo = [23, 43, 543, 541, 542, 544, 523, 5, 46, 12576, 56]
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
# # 实验4
# dic={"xiaom":{"kemu":833},
#      "xiaogang":{"kemu":289}}
# di={"xiaoming":287,"xiaogang":249,"zhonfen":[287,249]}#,{"menke":536}
# print (dic)

# 2 The second question'
# sports={"wang","wu","bai","hun","li","zhang"},{"she","he","zhang","hun","xiao","wang"}
# junp=
# for alpha in sports:
#     print(alpha)#printing all the elements
# print("The names",sports[1])
# print("The names",sports[3])

# for beta in junp: 
#     print(beta)
# sports.intersection_update(junp)
# print(junp)
