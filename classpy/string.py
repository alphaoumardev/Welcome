name = "alphapumar diallo"
surname = "diallo"
for i in surname:
    if i in name:
        name = name.replace(i, "")
    print(name)

# "alphaahpla" is 回文
alpha = str(input("input a string:"))
for i in range(len(alpha)):
    j = len(alpha) - 1 - i
    if alpha[i] != alpha[j] or i >= j:
        break
if i >= j:
    print("The number is 回文 huiwen")
else:
    print("The string is not huiwen")
