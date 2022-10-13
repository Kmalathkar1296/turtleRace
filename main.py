import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make a bet', prompt='Which color turtle will win? Take a Guess: ')
colors = ['red', 'purple', 'green', 'blue', 'yellow', 'violet']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-235, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if user_bet == winning_color:
                print(f"You have won {winning_color}")
            else:
                print(f"you have lost. Winner is {winning_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


def move_forwards():
    new_turtle.forward(10)


def move_backwards():
    new_turtle.backward(10)


def turn_left():
    new_turtle.left(10)
    new_turtle.forward(10)


def turn_right():
    new_turtle.right(10)
    new_turtle.forward(10)


def clear():
    new_turtle.clear()
    new_turtle.penup()
    new_turtle.home()
    new_turtle.pendown()


screen.listen()

screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()
