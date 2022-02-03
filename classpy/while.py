num = int(input("Please input a number"))
i = 1
sum = 0
while i < num:
    sum += i
    i = i + 1
print(sum)

a = 0
while a <= 500:
    sum += a
    a = a + 2
print(sum)

for i in range(101):
    sum += i
print("The sum in range 101", sum)
