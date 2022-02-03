alpha = eval(input("Please input your score: "))
if alpha >= 90:
    print("优")
elif 80 <= alpha < 90:
    print("良")
elif 70 <= alpha < 80:
    print("中")
elif 60 <= alpha < 70:
    print("ji ge ")
elif alpha < 60:
    print("fail the exam")
else:
    print("Dont mind about that person age ")
    # Notice that we can nest the (if)statement by the way
    # and notice in python the (elif)statement is the else if of the other languages
    # it's just it syntax is different from the others
