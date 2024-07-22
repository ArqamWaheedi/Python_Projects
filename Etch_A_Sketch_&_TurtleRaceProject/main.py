from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clockwise():
    tim.setheading(tim.heading() - 20)


def counter_clockwise():
    tim.setheading(tim.heading() + 20)

def clear():
    tim.reset()


screen.onkey(move_forward, key='w')
screen.onkey(move_backward, key='s')
screen.onkey(clockwise, key='d')
screen.onkey(counter_clockwise, key='a')
screen.onkey(clear, key='c')
screen.exitonclick()
