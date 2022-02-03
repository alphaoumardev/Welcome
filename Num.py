# import pymongo
import pip
# from bumpy import random
import numpy as np
import nose as you
# import conda

# print(conda.__version__)
# print(np.pi)
# print(np.__version__)
# print(you.__version__)
# print(pip.__version__)
arrays = np.array([32, 43, 6, 34, 4, 54, 56, 54, 3, 72])
print(arrays)
print(type(arrays))
arr = np.array([[1, 2, 4, 5], [4, 6, 3, 7, ], [45, 54, 65, [4, 65]]])
print(arr)
print(arr.ndim)
print(arrays.ndim)
print(arrays[2])
print(arrays[3] + arrays[4])
print(arr[0, 3])  # To index the array that is 5
print(arrays[2:7]), print(arrays[3:])  # to slice the array 1D
print(arrays[2:4:7]), print(arrays[::5]), print(arrays[1::4])  # to step the slcing

print(arr[1:3:4])
print(type(arr)), print(arrays.dtype)  # The datatype of an array
ty = arrays.astype('f')  # To covert the integer to float
print(ty.dtype)  # the datatype will be float
bol = arrays.astype(bool)
print(bol.dtype)
print("The view of the array", arr.view()), print("It's copy", arrays.copy())
print("The shape of the array", arrays.shape)
# print("The shape of the array",arrays.reshape(2,1))
for alpha in arrays:
    print("The array element ", alpha)
for oumar in arr:
    for diallo in oumar:
        print("The array element in the arr tuple", diallo)
        # for me in diallo:
        # print("The third part of the element",me)
for ar in arr:
    print("The array ", ar)
an_arr = np.array([23, 45, 6, 3, 7, 3, 5, [54, 46, 23, 6, ], [43, 65, 3, 56, 3]])
for the_array in np.ndenumerate(an_arr):
    print("The enumeration of the object", the_array)
# axis=1 is for dimension 1 array
ar = np.array([12, 5, 56, 23, 65, 34])
are = np.array([45, -65, 4, -5, -45, 3])
concat = np.concatenate((ar, are))
print("The concatenation", concat)
the_concat = np.stack((ar, are))
print("stacking", the_concat)
hstacking = np.hstack((ar, are))
print("Hstacking", hstacking)
stacking = np.vstack((ar, are))
print("Vstacking", stacking)
dstacking = np.dstack((ar, are))
print("Dstacking", dstacking)

print("To slipt the array", np.array_split(ar, 5))  # to split the array
print("To research a array value", np.where(ar % 2 == 0))
print("To research a array value", np.where(ar == 56))
print(np.searchsorted(ar, 34))

print("Sorting the array element", np.sort(ar))
print(np.sort(arrays))

bo = [True, False, True, False, False, True]
print(are[bo])

# The random number
# print(random.randint(100))
# print(random.choice(are))
# print(random.Generator)
# import turtle
# turtle.speed(fastest)
# turtle.pensize(1)
# for y in range(250):
#     turtle.forward(3*y)
#     tutle.lef(20)
#     turtle.right(180)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["mydatabase"]
# conca=np.concatenate((are+ar))
# print(conca)

# print("The shuffle of the array", random.shuffle(are))
# print("It's permutation", random.permutation(are))
