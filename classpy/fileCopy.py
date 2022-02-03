import copy

from numpy import sort


def printtext(copyFile):
    for row in copyFile:
        print(row)


text = open("Daily.txt", "r", encoding="utf-8")
text2 = copy.copy(text)
printtext(text)
print(text2.readlines())

with open("marks.text", "r", encoding="utf-8") as li:
    print(li.read())
    alpha = li.copy()
    alpha = open("sorted.txt", "a", encoding="utf-8")
    alpha.write(sort(key=lambda x: x[1], reverse=True))
    alpha.close()
    print(alpha.read())
# Open the file and overwrite the content
wear = open("alpha.txt", "w")
wear.write("You are the one who make me smile")
wear.close()
wear = open("Daily.txt", "r")
print(wear.read())
