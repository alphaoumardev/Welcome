import random

count = random.randint(0, 4)
print(count)

me = int(input("please input the number"))
if me == count:
    print("You get it")
elif me:
    print("You lose it")
alpha = 1
while alpha <= 10:
    print("媳妇我错了")
    break

a = 0
result = 0
while a >= 10 & a <= 20:
    result += a
    if a % 2 == 0:
        print(result)
    break

print("^")
print("^" * 2)
print("^" * 3), print("^" * 4), print("^" * 5), print("^" * 6), print("^" * 7)

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d" % (j, i, j * i), end=' ')
        j += 1
    print()
    i += 1
    break
