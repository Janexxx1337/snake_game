from turtle import Screen, Turtle
x_positions = [0, -20, -40]

segments = []




class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()



    def create_snake(self):
        for i in range(0, 3):
            turtle = Turtle(shape='square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(y=0, x=x_positions[i])
            self.segments.append(turtle)
