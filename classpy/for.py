myDict = {1: "python", 2: "javascript", 3: "java", 4: "springBoot", 5: "React"}
for a in myDict.items():
    print(a)
for i in myDict:
    print(i)
for m in myDict.keys():
    print(m)
for n in myDict.values():
    print(n)
# making sum with the for loop 
sum = 0
for alpha in range(501):
    sum += alpha
print(sum)

the_sum = 1
for mu in range(1, 21):
    the_sum *= mu
print(the_sum)

for i in range(40):
    if i == 30:
        break
    print(i)

for i in "Alpha oumar diallo":
    if i == "i":
        continue
    print(i)
for ra in range(100, 300):
    if ra % 7 != 0 and ra % 11 != 0:
        continue
    print(ra)
