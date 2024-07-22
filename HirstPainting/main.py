import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
# for n in range(len(colors)):
#     first_color = colors[n]
#     rgb = first_color.rgb
#     (red, blue, green) = (rgb[0], rgb[1], rgb[2])
#     color_list.append((red, blue, green))
# print(color_list)
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208)
              , (168, 99, 102)]

tim = Turtle()
screen = Screen()
tim.ht()
tim.speed('fastest')
tim.teleport(-200, -200)
y = -200
for _ in range(10):
    for n in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    y += 50
    tim.teleport(-200, y)

screen.exitonclick()
