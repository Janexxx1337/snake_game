from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


x_positions = [0, -20, -40]

segments = []


for i in range(0, 3):
    turtle = Turtle(shape='square')
    turtle.color('white')
    turtle.penup()
    turtle.goto(y=0, x=x_positions[i])
    segments.append(turtle)




game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):

        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)

screen.exitonclick()

