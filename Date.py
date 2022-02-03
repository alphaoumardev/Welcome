import math
import datetime

alpha = datetime.datetime.now()
oumar = datetime.datetime(2020, 8, 20)
print(oumar)
# diallo=datetime.datetime.tomorrow()
# print(diallo)
print(alpha.strftime("%A")), print(alpha.strftime("%B")), print(alpha.strftime("%C"))
print(alpha.strftime("%X")), print(alpha.strftime("%M")), print(alpha.strftime("%Y"))
print(alpha.strftime("%p")), print(alpha.strftime("%z")), print(alpha.strftime("%c"))

print(max(32, 34))
tuples = [534, 543, 64, 43, 65, 57, 84, 35, 768, 456, 89, ]
print(max(tuples))
print(min(tuples))
print((min(tuples) + max(tuples)) / 2)

print(abs(tuples[1]))
print(abs(tuples[-1]))

print(pow(23, 3))
print("The power of 2*2 is going to be ", pow(2, 2))

print(math.sqrt(64))  # At this position we must add the "math" module
print(math.ceil(2.5))
print(math.floor(34.2))
print(math.pi)
