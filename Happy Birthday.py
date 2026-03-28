import turtle
import time


screen = turtle.Screen()
screen.title("Happy Birthday!")
screen.bgcolor("Navy")
screen.setup(width=800, height=600)


t = turtle.Turtle()
t.hideturtle()
t.speed(3)


def write_text(text, color, size, y_pos):
    t.penup()
    t.goto(0, y_pos)
    t.color(color)
    t.pendown()
    t.write(text, align="center", font=("Shelley Fond", size, "bold"))


write_text("Happy Birthday !", "orange", 40, 50)
time.sleep(1)


write_text("Alexis", "blue", 30, -20)



colors = ["red", "yellow", "green", "purple", "orange", "blue"]
for i in range(10):
    for color in colors:
        write_text("🎂 🎈 ✨ 🎉", color, 50, -100)
        time.sleep(0.2)


turtle.done()
