###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle
import random
from turtle import Turtle, Screen

# Object Declaration
t = Turtle()
turtle.colormode(255)
t.speed("fastest")
t.hideturtle()
t.penup()


# Function Section
def printing_colors():
    for i in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)


def moving_up():
    t.setheading(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.setheading(0)


def moving_center():
    t.setheading(225)
    t.forward(300)
    t.setheading(0)



# Main Code Section
color_list = [(240, 241, 245), (236, 243, 239), (149, 50, 75), (222, 136, 201), (53, 123, 93), (170, 41, 154),
              (138, 20, 31), (134, 184, 163), (197, 73, 92), (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98),
              (232, 165, 176), (160, 158, 142), (54, 50, 45), (101, 77, 75), (183, 171, 205), (36, 74, 60),
              (19, 89, 86), (82, 129, 148), (147, 19, 17), (27, 102, 68), (12, 64, 70), (107, 153, 127),
              (176, 208, 192), (168, 102, 99)]
moving_center()
for _ in range(10):
    printing_colors()
    moving_up()

my_screen = Screen()
my_screen.exitonclick()
