import turtle
from turtle import Turtle
import pandas as pd

tom = Turtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guess = []
while len(guess) < 50:
    answer = screen.textinput(title=f"{len(guess)}/50 States Correct", prompt="What's another state's name")
    state = data[data["state"] == answer.title()]
    x_coor = state.x
    y_coor = state.y
    if answer.title() == "Exit":
        break
    if answer.title() in all_states:
        tom.penup()
        tom.hideturtle()
        tom.goto(int(x_coor), int(y_coor))
        tom.write(answer)
        guess.append(answer.title())

miss = [n for n in all_states if n not in guess]
print(guess)
new_data = pd.DataFrame(miss)
new_data.to_csv("learn.csv")


screen.exitonclick()
