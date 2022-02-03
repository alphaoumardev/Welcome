import turtle

alpha = turtle.Pen()
turtle.bgcolor("black")
sides = 10
colors = ["red", "orange", "green", "blue", "brown", "cyan", "purple", "yellow", "skyblue", "white"]
for oumar in range(360):
    alpha.pencolor(colors[oumar % sides])
    alpha.forward(oumar * 3 / sides + oumar)
    alpha.right(360 / sides + 1)
    alpha.left(360/sides+360)
    alpha.width(oumar * sides / 200)
    alpha.speed(500)
    # alpha.time(500)
    # alpha.date()
