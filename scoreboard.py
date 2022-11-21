from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial',22,'normal')



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score}: ", False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)


    def increaseScore(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
