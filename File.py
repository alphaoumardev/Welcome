import os

# alpha= open("Daily.txt","r")
# print(alpha.read())
alpha = open("Daily.txt", "a")
alpha.write(" i will always be by your side")
alpha.close()
alpha = open("Daily.txt", "r")
print(alpha.read())

# Open the file and overwrite the content
alpha = open("Daily.txt", "w")
alpha.write("You are the one who make me smile")
alpha.close()
alpha = open("Daily.txt", "r")
print(alpha.read())

# oumar=open("The_daily.txt","x")
oumar = open("The_daily.txt", "w")
oumar.write("As i said you still the one who make me smile so i really love you ")
oumar.close()
oumar = open("The_daily.txt", "r")
print(oumar.read())

# diallo=open("Journey.txt","x")
diallo = open("Journey.txt", "w")
diallo.write("The second file that has been created instead ")
diallo.close()
diallo = open("Journey.txt", "r")
print(diallo.read())

# To delete a file that exist
if os.path.exists("you.txt"):
    os.remove("you.txt")
else:
    print("The file does not exist")

# os.rmdir("new")
