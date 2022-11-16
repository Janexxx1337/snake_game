from turtle import Screen, Turtle
x_positions = [0, -20, -40]
move_distance = 20



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

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(move_distance)